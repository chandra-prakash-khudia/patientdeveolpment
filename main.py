import streamlit as st
import re
import json
from typing import Dict, Any
from ocr_utils import sort_text_row_col
from llm_utils import LlamaAgent, TOOLS_SYSTEM_PROMPT_STRUCTURE, TOOLS_SYSTEM_PROMPT_JSON
from db import create_database, insert_patient_record
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

def main():
    st.set_page_config(page_title="Medical Form Processor", layout="wide")
    st.title("Medical Form Processor")
    
    # Initialize the database
    create_database()
        #  File upload section
    uploaded_file = st.file_uploader("Upload Patient Form (JPG/JPEG)", type=["jpg", "jpeg"])
    json_data=""
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
            with st.status("🧠 Processing document...", expanded=True) as status:
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
                json_data = json_agent._query_ollama(structured_text)
        except Exception as e:
               st.error(f"❌ Processing failed: {str(e)}")
    
    llm_output =json_data
    
    if llm_output:
        try:
            # Extract and validate JSON from LLM output
            data = extract_json(llm_output)
            st.success("JSON extracted and validated!")
            st.json(data)
            
            # Build and display the editable form
            updated_data = build_editable_form(data)
            if updated_data is not None:
                st.write("### Updated Data")
                st.json(updated_data)
                # Optionally, perform database upsert:
                try:
                    insert_patient_record(updated_data)
                    st.success("Patient record saved successfully!")
                except Exception as db_error:
                    st.error(f"Error saving record to database: {db_error}")
        except Exception as e:
            st.error(f"Processing Error: {e}")

if __name__ == "__main__":
    main()
