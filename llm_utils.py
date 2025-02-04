import ollama
import json
from typing import Dict, Any

#

TOOLS_SYSTEM_PROMPT_STRUCTURE = (
    """
"You are a **medical data structuring agent**.
The user will provide OCR-extracted text from a patient registration form.

### **Your Task:**
1. Analyze the text and extract relevant medical information.
2. Structure the extracted text into **key-value pairs** based on predefined fields.
3. Ensure logical grouping of data using  **context clues**.

### **Output Format:**
EXAMPLE format where i provied keys and you will natch values to below keys;

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
    "Physician": "",
    "AdmittingPhysician": "",
    "DeliveryDueDate": ""
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

Return the data in the  key-value format:   """
)
TOOLS_SYSTEM_PROMPT_JSON = ("""
 You will receive structured text in the form of key-value pairs.
Your task is to convert these key-value pairs into a **valid JSON object**, following these rules:

1. **Maintain Data Integrity**  Ensure that all extracted values are correctly mapped to appropriate JSON keys.
2. **Use Proper Data Types**  Convert numerical values to numbers, and use `null` for missing data.
3. **Ensure Valid JSON**  The output must be syntactically correct and properly formatted.
4. **Do Not Add Extra Commentary**  Only return the JSON output without explanations.
dont use intelligence to guess just keep what it is .
""")

def __init__(self, name: str, instructions: str):
    self.name = name
    self.instructions = instructions
    try:
        self.client = ollama
        self.client.list()  # Test connection
    except Exception as e:
        raise RuntimeError(f"Ollama initialization failed: {str(e)}")

     
class LlamaAgent:
    def __init__(self, name: str, instructions: str):
        self.name = name
        self.instructions = instructions
        # Initialize Ollama client here
        self.client = ollama  # Direct use if ollama is properly configured

    def _query_ollama(self, prompt: str) -> str:
        """Get structured response from Ollama."""
        try:
            response = self.client.chat(
                model="llama3.2",  # Fixed model name (common Ollama model name format)
                messages=[
                    {"role": "system", "content": self.instructions},
                    {"role": "user", "content": prompt},
                ],
                options={
                    "temperature": 0  # Added for better structured output
                }
            )
            return response['message']['content']
        except Exception as e:
            raise RuntimeError(f"Ollama API Error: {str(e)}")