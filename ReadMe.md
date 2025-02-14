
# Project Documentation

This project implements a FastAPI application for processing medical forms. The application includes authentication, OCR processing, and patient record handling using both SQLAlchemy and SQLite. Below is the documentation for each file.

## auth.py
- **Purpose:**  
  Provides authentication functions and utilities.
- **Key Functions:**  
  - `verify_password`: Verifies if a provided plain password matches the hashed version.
  - `get_password_hash`: Generates a hashed password from a plain text input.
  - `create_access_token`: Creates a JWT access token with an expiration time.
  - `get_user_by_username`: Retrieves a user record from the database by username.
  - `authenticate_user`: Authenticates a user using the provided credentials.
- **Dependencies:**  
  Uses `jose`, `passlib`, and SQLAlchemy.

## database.py
- **Purpose:**  
  Configures the database connection using SQLAlchemy.
- **Key Components:**  
  - Creates a SQLite engine.
  - Sets up a session factory (`SessionLocal`) for DB transactions.
  - Defines a declarative base (`Base`) to be inherited by SQLAlchemy models.
- **Usage:**  
  Imported by other modules to initialize database sessions and create tables.

## db_functions.py
- **Purpose:**  
  Contains functions to manage patient records using SQLite.
- **Key Functions:**  
  - `create_database`: Initializes the SQLite database and creates the `patients` table.
  - `insert_patient_record`: Inserts a new patient record into the `patients` table.
  - `search_patient_record_by_name`: Searches for a patient record by name using SQL filtering.
- **Error Handling:**  
  Catches and raises database errors appropriately.

## llm_utils.py
- **Purpose:**  
  Provides utility functions to work with large language models (LLMs) for processing medical data.
- **Key Components:**  
  - LLM system prompts (structured and JSON).
  - A class `LlamaAgent` to interface with an LLM.
  - `extract_json`: Extracts JSON data from a given string response.
  - `extract_name_via_llm`: Extracts a patient's name from a doctor's query via an LLM.
  - `generate_final_response`: Builds a final answer by combining doctor queries with patient records.
- **Usage:**  
  Used for natural language processing in patient data and response generation.

## main.py
- **Purpose:**  
  Serves as the entry point for the FastAPI application.
- **Key Endpoints:**  
  - **Signup (`/signup`):** Creates a new user.
  - **Login (`/token`):** Authenticates a user and generates an access token.
  - **Upload (`/upload`):** Receives patient form images, applies OCR, and prepares structured data.
  - **Save (`/save`):** Saves (inserts) a patient record into the SQLite database.
  - **Search (`/search`):** Searches for a patient record using a doctor's query.
- **Additional Details:**  
  Integrates CORS middleware and uses JWT-based authentication.

## models.py
- **Purpose:**  
  Defines SQLAlchemy models and Pydantic schemas.
- **Key Models:**  
  - **SQLAlchemy `User` Model:**  
    Represents a user in the database with fields such as `username`, `full_name`, and `hashed_password`.
  - **Pydantic Models:**  
    - `UserCreate`: Used for user creation.
    - `UserResponse`: Used for serializing user responses.
- **Usage:**  
  Integral to user authentication and data validation.

## ocr_utils.py
- **Purpose:**  
  Implements the Optical Character Recognition (OCR) functionality.
- **Key Function:**  
  - `sort_text_row_col`: Applies PaddleOCR to extract and then sort text from an image based on its row and column positions.
- **Usage:**  
  Called during the file upload process to extract text from patient form images.

---
