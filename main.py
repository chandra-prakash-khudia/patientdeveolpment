
import os
import shutil
from datetime import timedelta
from fastapi import FastAPI, File, UploadFile, HTTPException, Query, Depends, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import uvicorn
from sqlalchemy.orm import Session

from database import SessionLocal, engine, Base
from models import User, UserCreate, UserResponse
from auth import get_password_hash, create_access_token, authenticate_user
from db_functions import create_database, insert_patient_record, search_patient_record_by_name
from ocr_utils import sort_text_row_col
from llm_utils import LlamaAgent, extract_json, extract_name_via_llm, generate_final_response, TOOLS_SYSTEM_PROMPT_STRUCTURE, TOOLS_SYSTEM_PROMPT_JSON

# Create the SQLAlchemy tables (if not already created)
Base.metadata.create_all(bind=engine)
# Initialize the patient records database for SQLite
# create_database()

app = FastAPI(title="Medical Form Processor API with Auth")

# Allow CORS (adjust origins as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

# ------------- Endpoints --------------

@app.post("/signup", status_code=201, response_model=UserResponse)
def signup_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already taken")
    
    hashed_password = get_password_hash(user.password)
    new_user = User(username=user.username, full_name=user.full_name, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """
    Upload a patient form image. The API runs OCR and LLM processing
    to return a structured JSON representation along with the raw OCR text.
    """
    temp_dir = "temp_uploads"
    os.makedirs(temp_dir, exist_ok=True)
    temp_path = os.path.join(temp_dir, file.filename)
    with open(temp_path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    
    try:
        # Run OCR processing
        sorted_text = sort_text_row_col(temp_path)
        ocr_text = " ".join([" ".join(row) for row in sorted_text])
        print("OCR result:")
        print(ocr_text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"OCR processing failed: {e}")
    
    try:
        # Run LLM processing to structure data
        struct_agent = LlamaAgent(name="StructAgent", instructions=TOOLS_SYSTEM_PROMPT_STRUCTURE)
        structured_text = struct_agent._query_ollama(ocr_text)
        print("Structured text:")
        print(structured_text)

        json_agent = LlamaAgent(name="JSONAgent", instructions=TOOLS_SYSTEM_PROMPT_JSON)
        llm_output = json_agent._query_ollama(structured_text)
        print("JSON output:")
        print(llm_output)
        data = extract_json(llm_output)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM processing failed: {e}")
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)
    
    # Return both structured data and raw OCR text
    return JSONResponse(content=data)


@app.post("/save")
async def save_patient_record(record: dict):
    """
    Save (insert) a patient record into the SQLite database.
    """
    try:
        insert_patient_record(record)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save record: {e}")
    return {"message": "Patient record saved successfully."}

@app.get("/search")
async def search_patient(doctor_query: str = Query(..., description="Doctor's query containing the patient name.")):
    """
    Search for a patient record using a doctor's query.
    The API extracts the patient name, searches for the record,
    and returns a final response with the requested details.
    """
    try:
        name = extract_name_via_llm(doctor_query)
        records = search_patient_record_by_name(name)
        if not records:
            return {"message": "No records found for the given name."}
        patient_record = records[0]
        final_response = generate_final_response(doctor_query, patient_record)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Search processing failed: {e}")
    return {"final_response": final_response}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
