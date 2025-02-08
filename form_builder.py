import streamlit as st
from typing import Dict, Any

def get_value_ci(d: Dict[str, Any], key: str, default: str = "") -> str:
    """
    Retrieve a value from dictionary d using a case-insensitive key search.
    Leading/trailing whitespace is removed from keys before comparing.
    """
    for k, v in d.items():
        if k.strip().lower() == key.strip().lower():
            return v
    return default

def build_editable_form(data: Dict[str, Any]) -> Dict[str, Any]:
    """Dynamically build an editable form from JSON structure, using case-insensitive key retrieval."""
    updated_data = {}

    with st.form("medical_form"):
        # Patient Information
        st.subheader("🩺 Patient Information")
        patient_info = data.get("Patient", {})
        updated_data["Patient"] = {
            "Name": st.text_input("Full Name", get_value_ci(patient_info, "Name", "")),
            "DateOfBirth": st.text_input("Date of Birth", get_value_ci(patient_info, "DateOfBirth", "")),
            "SocialSecurityNumber": st.text_input("Social Security Number", get_value_ci(patient_info, "SocialSecurityNumber", "")),
            "Address": st.text_area("Address", get_value_ci(patient_info, "Address", "")),
            "City": st.text_input("City", get_value_ci(patient_info, "City", "")),
            "State": st.text_input("State", get_value_ci(patient_info, "State", "")),
            "Zip": st.text_input("ZIP Code", get_value_ci(patient_info, "Zip", "")),
            "HomePhone": st.text_input("Home Phone", get_value_ci(patient_info, "HomePhone", "")),
            "Sex": st.selectbox(
                        "Sex",
                        ["Male", "Female", "Other"],
                        index=["Male", "Female", "Other"].index(get_value_ci(patient_info, "Sex", "Male"))
                   ),
            "Race": st.text_input("Race", get_value_ci(patient_info, "Race", "")),
            "MaritalStatus": st.text_input("Marital Status", get_value_ci(patient_info, "MaritalStatus", "")),
            "Religion": st.text_input("Religion", get_value_ci(patient_info, "Religion", "")),
            "EmployerName": st.text_input("Employer Name", get_value_ci(patient_info, "EmployerName", "")),
            "EmployerPhone": st.text_input("Employer Phone", get_value_ci(patient_info, "EmployerPhone", "")),
        }

        # Spouse/Significant Other Information
        st.subheader("💑 Spouse/Significant Other Information")
        spouse_info = data.get("Spouse/SignificantOther", {})
        updated_data["Spouse/SignificantOther"] = {
            "Name": st.text_input("Spouse Name", get_value_ci(spouse_info, "Name", "")),
            "DateOfBirth": st.text_input("Spouse DOB", get_value_ci(spouse_info, "DateOfBirth", "")),
            "SocialSecurityNumber": st.text_input("Spouse SSN", get_value_ci(spouse_info, "SocialSecurityNumber", "")),
            "Address": st.text_area("Spouse Address", get_value_ci(spouse_info, "Address", "")),
            "City": st.text_input("Spouse City", get_value_ci(spouse_info, "City", "")),
            "State": st.text_input("Spouse State", get_value_ci(spouse_info, "State", "")),
            "Zip": st.text_input("Spouse ZIP Code", get_value_ci(spouse_info, "Zip", "")),
            "HomePhone": st.text_input("Spouse Home Phone", get_value_ci(spouse_info, "HomePhone", "")),
            "EmployerName": st.text_input("Spouse Employer Name", get_value_ci(spouse_info, "EmployerName", "")),
            "EmployerPhone": st.text_input("Spouse Employer Phone", get_value_ci(spouse_info, "EmployerPhone", "")),
        }

        # Next of Kin Information
        st.subheader("👨‍👩‍👦 Next of Kin Information")
        next_of_kin_info = data.get("Next of Kin", {})
        updated_data["Next of Kin"] = {
            "Name": st.text_input("Next of Kin Name", get_value_ci(next_of_kin_info, "Name", "")),
            "RelationshipToPatient": st.text_input("Relationship to Patient", get_value_ci(next_of_kin_info, "RelationshipToPatient", "")),
            "DateOfBirth": st.text_input("Next of Kin DOB", get_value_ci(next_of_kin_info, "DateOfBirth", "")),
            "SocialSecurityNumber": st.text_input("Next of Kin SSN", get_value_ci(next_of_kin_info, "SocialSecurityNumber", "")),
            "Address": st.text_area("Next of Kin Address", get_value_ci(next_of_kin_info, "Address", "")),
            "City": st.text_input("Next of Kin City", get_value_ci(next_of_kin_info, "City", "")),
            "State": st.text_input("Next of Kin State", get_value_ci(next_of_kin_info, "State", "")),
            "Zip": st.text_input("Next of Kin ZIP Code", get_value_ci(next_of_kin_info, "Zip", "")),
            "HomePhone": st.text_input("Next of Kin Home Phone", get_value_ci(next_of_kin_info, "HomePhone", "")),
            "EmployerName": st.text_input("Next of Kin Employer Name", get_value_ci(next_of_kin_info, "EmployerName", "")),
            "EmployerPhone": st.text_input("Next of Kin Employer Phone", get_value_ci(next_of_kin_info, "EmployerPhone", "")),
        }

        # Insurance Information
        st.subheader("🏥 Primary Insurance Information")
        insurance_info = data.get("PrimaryInsurance", {})
        updated_data["PrimaryInsurance"] = {
            "CarrierName": st.text_input("Carrier Name", get_value_ci(insurance_info, "CarrierName", "")),
            "SubscriberName": st.text_input("Subscriber Name", get_value_ci(insurance_info, "SubscriberName", "")),
            "PolicyNumber": st.text_input("Policy Number", get_value_ci(insurance_info, "PolicyNumber", "")),
            "GroupName": st.text_input("Group Name", get_value_ci(insurance_info, "GroupName", "")),
            "GroupNumber": st.text_input("Group Number", get_value_ci(insurance_info, "GroupNumber", "")),
        }

        # Submit button
        if st.form_submit_button("💾 Save Patient Record"):
            return updated_data

    return None
