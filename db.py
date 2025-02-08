import sqlite3
import json
from typing import Dict, Any

def create_database():
    """Initialize database with proper schema"""
    conn = sqlite3.connect('medical_records.db')
    c = conn.cursor()
    # c.execute('DROP TABLE IF EXISTS patients')

    c.execute('''
        CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ssn TEXT,
        patient_name TEXT,
        patient_data TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
    ''')
    
    conn.commit()
    conn.close()

def insert_patient_record(data: Dict[str, Any]):
    """Insert patient record into the database along with a normalized patient name."""
    try:
        patient = data.get("Patient", {})
        ssn = patient.get("SocialSecurityNumber", "")
        patient_name = patient.get("Name", "")
        if not ssn:
            raise ValueError("Social Security Number is required in the patient data.")
        
        conn = sqlite3.connect('medical_records.db')
        c = conn.cursor()
        
        c.execute('''
            INSERT INTO patients (ssn, patient_name, patient_data)
            VALUES (?, ?, ?)
        ''', (ssn, patient_name, json.dumps(data)))
        
        conn.commit()
    except sqlite3.Error as e:
        raise RuntimeError(f"Database error: {str(e)}")
    finally:
        conn.close()

# def search_patient_record_by_name(name: str):
#     """Search for patient records by the normalized patient_name column using a case-insensitive match."""
#     conn = sqlite3.connect('medical_records.db')
#     c = conn.cursor()
#     query = "SELECT patient_data FROM patients WHERE LOWER(patient_name) = ?"
#     param = name.lower()
#     c.execute(query, (param,))
#     rows = c.fetchall()
#     conn.close()
    
#     results = []
#     for row in rows:
#         try:
#             results.append(json.loads(row[0]))
#         except json.JSONDecodeError:
#             continue
#     return results

def search_patient_record_by_name(name: str):
    """Search for patient records by filtering the JSON's Patient->Name field in Python."""
    conn = sqlite3.connect('medical_records.db')
    c = conn.cursor()
    query = "SELECT patient_data FROM patients"

    c.execute(query)
    rows = c.fetchall()
    print(rows)
    conn.close()
    
    results = []
    for row in rows:
        try:
            record = json.loads(row[0])
            patient_name = record.get("Patient", {}).get("Name", "")
            # Use a case-insensitive exact match or partial match as needed.
            if patient_name.lower() == name.lower():
                results.append(record)
        except json.JSONDecodeError:
            continue
    return results
