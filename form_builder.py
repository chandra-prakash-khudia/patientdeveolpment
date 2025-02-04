import streamlit as st
from typing import Dict, Any

def build_editable_form(data: Dict[str, Any]) -> Dict[str, Any]:
    """Dynamically build an editable form from JSON structure."""
    updated_data = {}

    with st.form("medical_form"):
        # Patient Information
        st.subheader("🩺 Patient Information")
        patient_info = data.get("Patient", {})
        updated_data["Patient"] = {
            "Name": st.text_input("Full Name", patient_info.get("Name", "")),
            "DateOfBirth": st.text_input("Date of Birth", patient_info.get("DateOfBirth", "")),
            "SocialSecurityNumber": st.text_input("Social Security Number", patient_info.get("SocialSecurityNumber", "")),
            "Address": st.text_area("Address", patient_info.get("Address", "")),
            "City": st.text_input("City", patient_info.get("City", "")),
            "State": st.text_input("State", patient_info.get("State", "")),
            "Zip": st.text_input("ZIP Code", patient_info.get("Zip", "")),
            "HomePhone": st.text_input("Home Phone", patient_info.get("HomePhone", "")),
            "Sex": st.selectbox("Sex", ["Male", "Female", "Other"], index=["Male", "Female", "Other"].index(patient_info.get("Sex", "Male"))),
            "Race": st.text_input("Race", patient_info.get("Race", "")),
            "MaritalStatus": st.text_input("Marital Status", patient_info.get("MaritalStatus", "")),
            "Religion": st.text_input("Religion", patient_info.get("Religion", "")),
            "EmployerName": st.text_input("Employer Name", patient_info.get("EmployerName", "")),
            "EmployerPhone": st.text_input("Employer Phone", patient_info.get("EmployerPhone", "")),
        }

        # Spouse/Significant Other Information
        st.subheader("💑 Spouse/Significant Other Information")
        spouse_info = data.get("Spouse/SignificantOther", {})
        updated_data["Spouse/SignificantOther"] = {
            "Name": st.text_input("Spouse Name", spouse_info.get("Name", "")),
            "DateOfBirth": st.text_input("Spouse DOB", spouse_info.get("DateOfBirth", "")),
            "SocialSecurityNumber": st.text_input("Spouse SSN", spouse_info.get("SocialSecurityNumber", "")),
            "Address": st.text_area("Spouse Address", spouse_info.get("Address", "")),
            "City": st.text_input("Spouse City", spouse_info.get("City", "")),
            "State": st.text_input("Spouse State", spouse_info.get("State", "")),
            "Zip": st.text_input("Spouse ZIP Code", spouse_info.get("Zip", "")),
            "HomePhone": st.text_input("Spouse Home Phone", spouse_info.get("HomePhone", "")),
            "EmployerName": st.text_input("Spouse Employer Name", spouse_info.get("EmployerName", "")),
            "EmployerPhone": st.text_input("Spouse Employer Phone", spouse_info.get("EmployerPhone", "")),
        }

        # Next of Kin Information
        st.subheader("👨‍👩‍👦 Next of Kin Information")
        next_of_kin_info = data.get("Next of Kin", {})
        updated_data["Next of Kin"] = {
            "Name": st.text_input("Next of Kin Name", next_of_kin_info.get("Name", "")),
            "RelationshipToPatient": st.text_input("Relationship to Patient", next_of_kin_info.get("RelationshipToPatient", "")),
            "DateOfBirth": st.text_input("Next of Kin DOB", next_of_kin_info.get("DateOfBirth", "")),
            "SocialSecurityNumber": st.text_input("Next of Kin SSN", next_of_kin_info.get("SocialSecurityNumber", "")),
            "Address": st.text_area("Next of Kin Address", next_of_kin_info.get("Address", "")),
            "City": st.text_input("Next of Kin City", next_of_kin_info.get("City", "")),
            "State": st.text_input("Next of Kin State", next_of_kin_info.get("State", "")),
            "Zip": st.text_input("Next of Kin ZIP Code", next_of_kin_info.get("Zip", "")),
            "HomePhone": st.text_input("Next of Kin Home Phone", next_of_kin_info.get("HomePhone", "")),
            "EmployerName": st.text_input("Next of Kin Employer Name", next_of_kin_info.get("EmployerName", "")),
            "EmployerPhone": st.text_input("Next of Kin Employer Phone", next_of_kin_info.get("EmployerPhone", "")),
        }

        # Insurance Information
        st.subheader("🏥 Primary Insurance Information")
        insurance_info = data.get("PrimaryInsurance", {})
        updated_data["PrimaryInsurance"] = {
            "CarrierName": st.text_input("Carrier Name", insurance_info.get("CarrierName", "")),
            "SubscriberName": st.text_input("Subscriber Name", insurance_info.get("SubscriberName", "")),
            "PolicyNumber": st.text_input("Policy Number", insurance_info.get("PolicyNumber", "")),
            "GroupName": st.text_input("Group Name", insurance_info.get("GroupName", "")),
            "GroupNumber": st.text_input("Group Number", insurance_info.get("GroupNumber", "")),
        }

        # Submit button
        if st.form_submit_button("💾 Save Patient Record"):
            return updated_data

    return None
