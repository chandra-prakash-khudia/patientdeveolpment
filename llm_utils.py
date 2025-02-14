# app/llm.py
import re
import json
from typing import Dict, Any
import ollama

# System prompts for LLM processing
TOOLS_SYSTEM_PROMPT_STRUCTURE = (
    """
"You are a **medical data structuring agent**.
The user will provide OCR-extracted text from a patient registration form.

### **Your Task:**
1. Analyze the text and extract relevant medical information.
2. Structure the extracted text into **key-value pairs** based on predefined fields.
3. Ensure logical grouping of data using **context clues**.

### **Output Format:**
EXAMPLE format where I provided keys and you will match values to the below keys;

{
  "Patient": {
    "Name": "",
    "DateOfBirth": "",
    "SocialSecurityNumber": "",
    "Address": "",
    "City": "",
    "State": "",
    "Zip": "",
    "HomePhone": "",
    "Sex": "",
    "Race": "",
    "MaritalStatus": "",
    "Religion": "",
    "EmployerName": "",
    "EmployerPhone": "",
    "Family Physician": "",
    "Admitting Physician": "",
    "DeliveryDueDate": " ",
    
  },
  "SpouseOrSignificantOther": {
    "Name": "",
    "DateOfBirth": "",
    "SocialSecurityNumber": "",
    "Address": "",
    "City": "",
    "State": "",
    "Zip": "",
    "HomePhone": "",
    "EmployerName": "",
    "EmployerPhone": ""
  },
  "NextOfKin": {
    "Name": "",
    "RelationshipToPatient": "",
    "DateOfBirth": "",
    "SocialSecurityNumber": "",
    "Address": "",
    "City": "",
    "State": "",
    "Zip": "",
    "HomePhone": "",
    "EmployerName": "",
    "EmployerPhone": ""
  },
  "PrimaryInsurance": {
    "CarrierName": "",
    "SubscriberName": "",
    "PolicyNumber": "",
    "GroupName": "",
    "GroupNumber": ""
  }
}

Return the data in the key-value format:"""
)

TOOLS_SYSTEM_PROMPT_JSON = ("""
You will receive structured text in the form of key-value pairs.
Your task is to convert these key-value pairs into a **valid JSON object** and remove unnecessary characters like _ , ( , )  and spacing inbetween fieldname like Next of kin to NextOfKin, following these rules:

1. **Maintain Data Integrity**: Ensure that all extracted values are correctly mapped to appropriate JSON keys.
2. **Use Proper Data Types**: Convert numerical values to numbers, and use `null` for missing data.
3. **Ensure Valid JSON**: The output must be syntactically correct and properly formatted.
4. **Do Not Add Extra Commentary**: Only return the JSON output without explanations.
dont use intelligence to guess just keep what it is.
""")

FINAL_RESPONSE_SYSTEM_PROMPT = """
You are a patient information response agent.
You are given a doctor's query and patient information in JSON format.
Your task is to provide an answer that extracts only the details requested in the query.
The answer should be a simple sentence that includes the required details.
Return only the required details without any extra commentary.
For example:
Doctor Query: "Give me the address and phone number of the patient."
Patient Information: {"Patient": {"Name": "John Doe", "Address": "123 Main Street", "HomePhone": "555-1234", ...}, ...}
Output: "the address is 123 Main Street and the phone number is 555-1234"
"""

class LlamaAgent:
    def __init__(self, name: str, instructions: str):
        self.name = name
        self.instructions = instructions
        self.client = ollama

    def _query_ollama(self, prompt: str) -> str:
        try:
            response = self.client.chat(
                model="llama3.2",
                messages=[
                    {"role": "system", "content": self.instructions},
                    {"role": "user", "content": prompt},
                ],
                options={"temperature": 0}
            )
            return response['message']['content']
        except Exception as e:
            raise RuntimeError(f"Ollama API Error: {str(e)}")

def extract_json(response: str) -> Dict[str, Any]:
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
    extraction_instructions = """
you are a human who is asked to extract the name of the patient from a doctor's query.
The doctor's query will be a sentence or question that contains the patient's name.
Your task is to extract only the patient's name from the query.
NO COMMENTS OR ADDITIONAL INFORMATION SHOULD BE PROVIDED.
Example:
Doctor's Query: "give me all details of chandra prakash"
Output: "CHANDRA PRAKASH"
"""
    name_agent = LlamaAgent(name="NameExtractionAgent", instructions=extraction_instructions)
    response = name_agent._query_ollama(prompt)
    return response.strip().strip('"')

def generate_final_response(doctor_prompt: str, patient_record: Dict[str, Any]) -> str:
    combined_input = f"Doctor Query: {doctor_prompt}\nPatient Information: {json.dumps(patient_record)}"
    response_agent = LlamaAgent(name="ResponseAgent", instructions=FINAL_RESPONSE_SYSTEM_PROMPT)
    response = response_agent._query_ollama(combined_input)
    return response.strip()
