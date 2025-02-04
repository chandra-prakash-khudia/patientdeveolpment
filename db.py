import sqlite3
import json
from typing import Dict, Any

def create_database():
    """Initialize database with proper schema"""
    conn = sqlite3.connect('medical_records.db')
    c = conn.cursor()
    c.execute('DROP TABLE IF EXISTS patients')

    c.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ssn TEXT,
            patient_data TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

def insert_patient_record(data: Dict[str, Any]):
    """Insert patient record into the database"""
    try:
        ssn = data.get("Patient", {}).get("SocialSecurityNumber", "")
        if not ssn:
            raise ValueError("Social Security Number is required in the patient data.")
        
        conn = sqlite3.connect('medical_records.db')
        c = conn.cursor()
        
        c.execute('''
            INSERT INTO patients (ssn, patient_data)
            VALUES (?, ?)
        ''', (ssn, json.dumps(data)))
        
        conn.commit()
    except sqlite3.Error as e:
        raise RuntimeError(f"Database error: {str(e)}")
    finally:
        conn.close()
