import streamlit as st
import re
import json
from typing import Dict, Any
from ocr_utils import sort_text_row_col
from llm_utils import LlamaAgent, TOOLS_SYSTEM_PROMPT_STRUCTURE, TOOLS_SYSTEM_PROMPT_JSON
from db import create_database, insert_patient_record , search_patient_record_by_name
from form_builder import build_editable_form

def extract_json(response: str) -> Dict[str, Any]:
    """
    Extract the JSON object from the LLM response.
    This function uses a regex to find the first occurrence of a JSON object (from '{' to '}')
    and returns it as a Python dictionary.
    """
    json_pattern = re.compile(r"(\{(?:.|\n)*\})", re.MULTILINE)
    match = json_pattern.search(response)
    if match:
        json_str = match.group(1)
        try:
            return json.loads(json_str)
        except json.JSONDecodeError as e:
            raise ValueError(f"Extracted JSON is invalid: {e}")
    else:
        raise ValueError("No JSON object could be extracted from the response.")
def extract_name_via_llm(prompt: str) -> str:
    """
    Uses an LLM to extract the patient name from the doctor's prompt.
    The LLM is instructed to return only the patient's name.
    """
    extraction_instructions = """
    you are a human who is asked to extract the name of the patient from a doctor's query.
    The doctor's query will be a sentence or question that contains the patient's name.
    Your task is to extract only the patient's name from the query.
    Doctor can ask you anything but you have to return only the patient's name.
    NO COMMENTS OR ADDITIONAL INFORMATION SHOULD BE PROVIDED.
    Example:
    Doctor's Query: "give me all details of chandra prakash
    Output: "CHANDRA PRAKASH"
    Doctor's Query: "what is the age of chandra prakash"
    Output: "CHANDRA PRAKASH"
    Doctor's Query: "give me   contact details of spouse   of chandra prakash"
    Output: "CHANDRA PRAKASH"
    """

    name_agent = LlamaAgent(name="NameExtractionAgent", instructions=extraction_instructions)
    response = name_agent._query_ollama(prompt)
    # Clean the response by stripping any surrounding whitespace or quotes.
    return response.strip().strip('"')

# def main():
#     st.set_page_config(page_title="Medical Form Processor", layout="wide")
#     st.title("Medical Form Processor")
    
#     # Initialize the database
#     create_database()
#         #  File upload section
#     uploaded_file = st.file_uploader("Upload Patient Form (JPG/JPEG)", type=["jpg", "jpeg"])
#     json_data=""
#     if uploaded_file:
#         # Temporary file handling
#         temp_path = "temp_form.jpg"
#         with open(temp_path, "wb") as f:
#             f.write(uploaded_file.getbuffer())
        
#         # Display uploaded image
#         st.image(temp_path, caption="Scanned Form Preview", use_column_width=True)
        
#         try:
#             # OCR Processing
#             with st.spinner("🔍 Extracting text from document..."):
#                 sorted_text = sort_text_row_col(temp_path)
#                 ocr_text = " ".join([" ".join(row) for row in sorted_text])
            
#             # LLM Processing
#             with st.status("🧠 Processing document...", expanded=True) as status:
#                 # Structure extraction
#                 struct_agent = LlamaAgent(
#                     name="StructAgent",
#                     instructions=TOOLS_SYSTEM_PROMPT_STRUCTURE
#                 )
#                 structured_text = struct_agent._query_ollama(ocr_text)
                
#                 # JSON conversion
#                 json_agent = LlamaAgent(
#                     name="JSONAgent",
#                     instructions=TOOLS_SYSTEM_PROMPT_JSON
#                 )
#                 json_data = json_agent._query_ollama(structured_text)
#         except Exception as e:
#                st.error(f"❌ Processing failed: {str(e)}")
    
#     llm_output =json_data
    
#     if llm_output:
#         try:
#             # Extract and validate JSON from LLM output
#             data = extract_json(llm_output)
#             st.success("JSON extracted and validated!")
#             st.json(data)
            
#             # Build and display the editable form
#             updated_data = build_editable_form(data)
#             if updated_data is not None:
#                 st.write("### Updated Data")
#                 st.json(updated_data)
#                 # Optionally, perform database upsert:
#                 try:
#                     insert_patient_record(updated_data)
#                     st.success("Patient record saved successfully!")
#                 except Exception as db_error:
#                     st.error(f"Error saving record to database: {db_error}")
#         except Exception as e:
#             st.error(f"Processing Error: {e}")

# if __name__ == "__main__":
#     main()

FINAL_RESPONSE_SYSTEM_PROMPT = """
You are a patient information response agent.
You are given a doctor's query and patient information in JSON format.
Your task is to provide a  answer that extracts only the details requested in the query.
The answer should be a simple sentence that includes the required details.
dont give in the form of json.
Return only the required details without any extra commentary
For example:
Doctor Query: "Give me the address and phone number of the patient."
Patient Information: {"Patient": {"Name": "John Doe", "Address": "123 Main Street", "HomePhone": "555-1234", ...}, ...}
Output: "the address is 123 Main Street and the phone number is 555-1234"
"""

def generate_final_response(doctor_prompt: str, patient_record: Dict[str, Any]) -> str:
    """
    Combine the doctor's prompt with the patient record and pass them to an LLM to generate a final answer.
    """
    combined_input = f"Doctor Query: {doctor_prompt}\nPatient Information: {json.dumps(patient_record)}"
    response_agent = LlamaAgent(name="ResponseAgent", instructions=FINAL_RESPONSE_SYSTEM_PROMPT)
    response = response_agent._query_ollama(combined_input)
    return response.strip()



def main():
    st.set_page_config(page_title="Medical Form Processor", layout="wide")
    st.title("Medical Form Processor")

    # Initialize the database
    create_database()

    # Let the user choose the operation mode
    operation = st.radio("Choose Operation Mode", ["Upload Document", "Search Patient Record"])

    llm_output = ""
    data = None

    if operation == "Upload Document":
        uploaded_file = st.file_uploader("Upload Patient Form (JPG/JPEG)", type=["jpg", "jpeg"])
        if uploaded_file:
            # Temporary file handling
            temp_path = "temp_form.jpg"
            with open(temp_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            # Display uploaded image
            st.image(temp_path, caption="Scanned Form Preview", use_column_width=True)

            try:
                # OCR Processing
                with st.spinner("🔍 Extracting text from document..."):
                    sorted_text = sort_text_row_col(temp_path)
                    ocr_text = " ".join([" ".join(row) for row in sorted_text])

                # LLM Processing
                with st.spinner("🧠 Processing document..."):
                    # Structure extraction
                    struct_agent = LlamaAgent(
                        name="StructAgent",
                        instructions=TOOLS_SYSTEM_PROMPT_STRUCTURE
                    )
                    structured_text = struct_agent._query_ollama(ocr_text)

                    # JSON conversion
                    json_agent = LlamaAgent(
                        name="JSONAgent",
                        instructions=TOOLS_SYSTEM_PROMPT_JSON
                    )
                    llm_output = json_agent._query_ollama(structured_text)
            except Exception as e:
                st.error(f"❌ Processing failed: {str(e)}")

            if llm_output:
                try:
                    # Extract and validate JSON from LLM output
                    data = extract_json(llm_output)
                    st.success("JSON extracted and validated!")
                    # st.json(data)
                except Exception as e:
                    st.error(f"JSON Extraction Error: {e}")
    elif operation == "Search Patient Record":
        doctor_prompt = st.text_input("Enter doctor prompt (e.g., 'I want the information of chandra prakash'):")
        if st.button("Search"):
            if doctor_prompt:
                with st.spinner("Extracting patient name using LLM..."):
                    name = extract_name_via_llm(doctor_prompt)
                st.write(f"Extracted patient name: **{name}**")
                st.info(f"Searching for patient records with name containing: **{name}**")
                records = search_patient_record_by_name(name)
                # st.write(records)
                if records:
                    # st.success(f"Found {len(records)} record(s).")
                    # For this example, we'll assume one record (or use the first one)
                    patient_record = records[0]
                    # st.json(patient_record)
                    
                    # Now generate a final response by combining the doctor's prompt and patient record.
                    with st.spinner("Generating final response..."):
                        final_response = generate_final_response(doctor_prompt, patient_record)
                    st.markdown("### Final Response")
                    st.write(final_response)
                else:
                    st.warning("No records found for the given name.")
            else:
                st.warning("Please enter a prompt.")


    # If we have JSON data from the extraction pipeline, allow editing and saving.
    if data:
        updated_data = build_editable_form(data)
        if updated_data is not None:
            st.write("### Updated Data")
            st.json(updated_data)
            # Optionally, save the updated record to the database
            try:
                insert_patient_record(updated_data)
                st.success("Patient record saved successfully!")
            except Exception as db_error:
                st.error(f"Error saving record to database: {db_error}")

if __name__ == "__main__":
    main()
