// // PatientForm.jsx
// import React, { useState } from "react";
// import "./App.css";

// // PatientForm.jsx


// const PatientForm = ({ patientData, onSave }) => {
//   const [formData, setFormData] = useState({
//     Patient: patientData.Patient || {},
//     SpouseOrSignificantOther: patientData.SpouseOrSignificantOther || {},
//     NextOfKin: patientData.NextOfKin || {},
//     PrimaryInsurance: patientData.PrimaryInsurance || {},
//   });

//   const handleChange = (section, field, value) => {
//     setFormData((prev) => ({
//       ...prev,
//       [section]: {
//         ...prev[section],
//         [field]: value,
//       },
//     }));
//   };

//   const handleSubmit = (e) => {
//     e.preventDefault();
//     onSave(formData);
//   };

//   return (
//     <form onSubmit={handleSubmit} className="patient-form">
//       <h2>Patient Information</h2>
//       <div className="form-section">
//         <label>
//           Name:
//           <input
//             type="text"
//             value={formData.Patient.Name || ""}
//             onChange={(e) => handleChange("Patient", "Name", e.target.value)}
//           />
//         </label>
//         <label>
//           Date of Birth:
//           <input
//             type="date"
//             value={formData.Patient.DateOfBirth || ""}
//             onChange={(e) =>
//               handleChange("Patient", "DateOfBirth", e.target.value)
//             }
//           />
//         </label>
//         <label>
//           Social Security Number:
//           <input
//             type="text"
//             value={formData.Patient.SocialSecurityNumber || ""}
//             onChange={(e) =>
//               handleChange("Patient", "SocialSecurityNumber", e.target.value)
//             }
//           />
//         </label>
//         <label>
//           Address:
//           <input
//             type="text"
//             value={formData.Patient.Address || ""}
//             onChange={(e) =>
//               handleChange("Patient", "Address", e.target.value)
//             }
//           />
//         </label>
//         <label>
//           City:
//           <input
//             type="text"
//             value={formData.Patient.City || ""}
//             onChange={(e) => handleChange("Patient", "City", e.target.value)}
//           />
//         </label>
//         <label>
//           State:
//           <input
//             type="text"
//             value={formData.Patient.State || ""}
//             onChange={(e) => handleChange("Patient", "State", e.target.value)}
//           />
//         </label>
//         <label>
//           Zip:
//           <input
//             type="text"
//             value={formData.Patient.Zip || ""}
//             onChange={(e) => handleChange("Patient", "Zip", e.target.value)}
//           />
//         </label>
//         <label>
//           Home Phone:
//           <input
//             type="text"
//             value={formData.Patient.HomePhone || ""}
//             onChange={(e) =>
//               handleChange("Patient", "HomePhone", e.target.value)
//             }
//           />
//         </label>
//         <label>
//           Sex:
//           <select
//             value={formData.Patient.Sex || ""}
//             onChange={(e) => handleChange("Patient", "Sex", e.target.value)}
//           >
//             <option value="">Select</option>
//             <option value="Male">Male</option>
//             <option value="Female">Female</option>
//             <option value="Other">Other</option>
//           </select>
//         </label>
//         <label>
//           Race:
//           <input
//             type="text"
//             value={formData.Patient.Race || ""}
//             onChange={(e) => handleChange("Patient", "Race", e.target.value)}
//           />
//         </label>
//         <label>
//           Marital Status:
//           <input
//             type="text"
//             value={formData.Patient.MaritalStatus || ""}
//             onChange={(e) =>
//               handleChange("Patient", "MaritalStatus", e.target.value)
//             }
//           />
//         </label>
//         <label>
//           Religion:
//           <input
//             type="text"
//             value={formData.Patient.Religion || ""}
//             onChange={(e) =>
//               handleChange("Patient", "Religion", e.target.value)
//             }
//           />
//         </label>
//         <label>
//           Employer Name:
//           <input
//             type="text"
//             value={formData.Patient.EmployerName || ""}
//             onChange={(e) =>
//               handleChange("Patient", "EmployerName", e.target.value)
//             }
//           />
//         </label>
//         <label>
//           Employer Phone:
//           <input
//             type="text"
//             value={formData.Patient.EmployerPhone || ""}
//             onChange={(e) =>
//               handleChange("Patient", "EmployerPhone", e.target.value)
//             }
//           />
//         </label>
//         <label>
//           Physician:
//           <input
//             type="text"
//             value={formData.Patient.Physician || ""}
//             onChange={(e) =>
//               handleChange("Patient", "Physician", e.target.value)
//             }
//           />
//         </label>
//         <label>
//           Admitting Physician:
//           <input
//             type="text"
//             value={formData.Patient.AdmittingPhysician || ""}
//             onChange={(e) =>
//               handleChange("Patient", "AdmittingPhysician", e.target.value)
//             }
//           />
//         </label>
//         <label>
//           Delivery Due Date:
//           <input
//             type="date"
//             value={formData.Patient.DeliveryDueDate || ""}
//             onChange={(e) =>
//               handleChange("Patient", "DeliveryDueDate", e.target.value)
//             }
//           />
//         </label>
//       </div>

//       <h2>Spouse/Significant Other Information</h2>
//       <div className="form-section">
//         <label>
//           Name:
//           <input
//             type="text"
//             value={formData.SpouseOrSignificantOther.Name || ""}
//             onChange={(e) =>
//               handleChange(
//                 "SpouseOrSignificantOther",
//                 "Name",
//                 e.target.value
//               )
//             }
//           />
//         </label>
//         <label>
//           Date of Birth:
//           <input
//             type="date"
//             value={formData.SpouseOrSignificantOther.DateOfBirth || ""}
//             onChange={(e) =>
//               handleChange(
//                 "SpouseOrSignificantOther",
//                 "DateOfBirth",
//                 e.target.value
//               )
//             }
//           />
//         </label>
//         <label>
//           Social Security Number:
//           <input
//             type="text"
//             value={formData.SpouseOrSignificantOther.SocialSecurityNumber || ""}
//             onChange={(e) =>
//               handleChange(
//                 "SpouseOrSignificantOther",
//                 "SocialSecurityNumber",
//                 e.target.value
//               )
//             }
//           />
//         </label>
//         <label>
//           Address:
//           <input
//             type="text"
//             value={formData.SpouseOrSignificantOther.Address || ""}
//             onChange={(e) =>
//               handleChange(
//                 "SpouseOrSignificantOther",
//                 "Address",
//                 e.target.value
//               )
//             }
//           />
//         </label>
//         <label>
//           City:
//           <input
//             type="text"
//             value={formData.SpouseOrSignificantOther.City || ""}
//             onChange={(e) =>
//               handleChange("SpouseOrSignificantOther", "City", e.target.value)
//             }
//           />
//         </label>
//         <label>
//           State:
//           <input
//             type="text"
//             value={formData.SpouseOrSignificantOther.State || ""}
//             onChange={(e) =>
//               handleChange("SpouseOrSignificantOther", "State", e.target.value)
//             }
//           />
//         </label>
//         <label>
//           Zip:
//           <input
//             type="text"
//             value={formData.SpouseOrSignificantOther.Zip || ""}
//             onChange={(e) =>
//               handleChange("SpouseOrSignificantOther", "Zip", e.target.value)
//             }
//           />
//         </label>
//         <label>
//           Home Phone:
//           <input
//             type="text"
//             value={formData.SpouseOrSignificantOther.HomePhone || ""}
//             onChange={(e) =>
//               handleChange("SpouseOrSignificantOther", "HomePhone", e.target.value)
//             }
//           />
//         </label>
//         <label>
//           Employer Name:
//           <input
//             type="text"
//             value={formData.SpouseOrSignificantOther.EmployerName || ""}
//             onChange={(e) =>
//               handleChange("SpouseOrSignificantOther", "EmployerName", e.target.value)
//             }
//           />
//         </label>
//         <label>
//           Employer Phone:
//           <input
//             type="text"
//             value={formData.SpouseOrSignificantOther.EmployerPhone || ""}
//             onChange={(e) =>
//               handleChange("SpouseOrSignificantOther", "EmployerPhone", e.target.value)
//             }
//           />
//         </label>
//       </div>

//       <h2>Next of Kin Information</h2>
//       <div className="form-section">
//         <label>
//           Name:
//           <input
//             type="text"
//             value={formData.NextOfKin.Name || ""}
//             onChange={(e) =>
//               handleChange("NextOfKin", "Name", e.target.value)
//             }
//           />
//         </label>
//         <label>
//           Relationship to Patient:
//           <input
//             type="text"
//             value={formData.NextOfKin.RelationshipToPatient || ""}
//             onChange={(e) =>
//               handleChange("NextOfKin", "RelationshipToPatient", e.target.value)
//             }
//           />
//         </label>
//         <label>
//           Date of Birth:
//           <input
//             type="date"
//             value={formData.NextOfKin.DateOfBirth || ""}
//             onChange={(e) =>
//               handleChange("NextOfKin", "DateOfBirth", e.target.value)
//             }
//           />
//         </label>
//         <label>
//           Social Security Number:
//           <input
//             type="text"
//             value={formData.NextOfKin.SocialSecurityNumber || ""}
//             onChange={(e) =>
//               handleChange("NextOfKin", "SocialSecurityNumber", e.target.value)
//             }
//           />
//         </label>
//         <label>
//           Address:
//           <input
//             type="text"
//             value={formData.NextOfKin.Address || ""}
//             onChange={(e) =>
//               handleChange("NextOfKin", "Address", e.target.value)
//             }
//           />
//         </label>
//         <label>
//           City:
//           <input
//             type="text"
//             value={formData.NextOfKin.City || ""}
//             onChange={(e) =>
//               handleChange("NextOfKin", "City", e.target.value)
//             }
//           />
//         </label>
//         <label>
//           State:
//           <input
//             type="text"
//             value={formData.NextOfKin.State || ""}
//             onChange={(e) =>
//               handleChange("NextOfKin", "State", e.target.value)
//             }
//           />
//         </label>
//         <label>
//           Zip:
//           <input
//             type="text"
//             value={formData.NextOfKin.Zip || ""}
//             onChange={(e) =>
//               handleChange("NextOfKin", "Zip", e.target.value)
//             }
//           />
//         </label>
//         <label>
//           Home Phone:
//           <input
//             type="text"
//             value={formData.NextOfKin.HomePhone || ""}
//             onChange={(e) =>
//               handleChange("NextOfKin", "HomePhone", e.target.value)
//             }
//           />
//         </label>
//         <label>
//           Employer Name:
//           <input
//             type="text"
//             value={formData.NextOfKin.EmployerName || ""}
//             onChange={(e) =>
//               handleChange("NextOfKin", "EmployerName", e.target.value)
//             }
//           />
//         </label>
//         <label>
//           Employer Phone:
//           <input
//             type="text"
//             value={formData.NextOfKin.EmployerPhone || ""}
//             onChange={(e) =>
//               handleChange("NextOfKin", "EmployerPhone", e.target.value)
//             }
//           />
//         </label>
//       </div>

//       <h2>Primary Insurance Information</h2>
//       <div className="form-section">
//         <label>
//           Carrier Name:
//           <input
//             type="text"
//             value={formData.PrimaryInsurance.CarrierName || ""}
//             onChange={(e) =>
//               handleChange("PrimaryInsurance", "CarrierName", e.target.value)
//             }
//           />
//         </label>
//         <label>
//           Subscriber Name:
//           <input
//             type="text"
//             value={formData.PrimaryInsurance.SubscriberName || ""}
//             onChange={(e) =>
//               handleChange("PrimaryInsurance", "SubscriberName", e.target.value)
//             }
//           />
//         </label>
//         <label>
//           Policy Number:
//           <input
//             type="text"
//             value={formData.PrimaryInsurance.PolicyNumber || ""}
//             onChange={(e) =>
//               handleChange("PrimaryInsurance", "PolicyNumber", e.target.value)
//             }
//           />
//         </label>
//         <label>
//           Group Name:
//           <input
//             type="text"
//             value={formData.PrimaryInsurance.GroupName || ""}
//             onChange={(e) =>
//               handleChange("PrimaryInsurance", "GroupName", e.target.value)
//             }
//           />
//         </label>
//         <label>
//           Group Number:
//           <input
//             type="text"
//             value={formData.PrimaryInsurance.GroupNumber || ""}
//             onChange={(e) =>
//               handleChange("PrimaryInsurance", "GroupNumber", e.target.value)
//             }
//           />
//         </label>
//       </div>
//       <button type="submit" className="save-button">
//         Save Record
//       </button>
//     </form>
//   );
// };

// export default PatientForm;


// PatientForm.jsx
import React, { useState, useEffect } from "react";

const PatientForm = ({ patientData, onSave }) => {
  // Helper function that normalizes keys in a section using a provided mapping.
  const normalizeSection = (sectionData, mapping) => {
    const normalized = {};
    for (const key in sectionData) {
      // Remove spaces, slashes, underscores and convert to lower case for matching.
      const lowerKey = key.toLowerCase().replace(/[\s\/_]/g, "");
      if (mapping[lowerKey]) {
        normalized[mapping[lowerKey]] = sectionData[key];
      }
    }
    return normalized;
  };

  // Mapping objects for each section.
  const patientMapping = {
    "name": "Name",
    "dateofbirth": "DateOfBirth",
    "socialsecuritynumber": "SocialSecurityNumber",
    "address": "Address",
    "city": "City",
    "state": "State",
    "zip": "Zip",
    "homephone": "HomePhone",
    "sex": "Sex",
    "race": "Race",
    "maritalstatus": "MaritalStatus",
    "religion": "Religion",
    "employername": "EmployerName",
    "employerphone": "EmployerPhone",
    "familyphysician": "FamilyPhysician",
    "admittingphysician": "AdmittingPhysician",
    "deliveryduedate": "DeliveryDueDate",
  };

  const spouseMapping = {
    "name": "Name",
    "dateofbirth": "DateOfBirth",
    "socialsecuritynumber": "SocialSecurityNumber",
    "address": "Address",
    "city": "City",
    "state": "State",
    "zip": "Zip",
    "homephone": "HomePhone",
    "employername": "EmployerName",
    "employerphone": "EmployerPhone",
  };

  const nextMapping = {
    "name": "Name",
    "relationshiptopatient": "RelationshipToPatient",
    "dateofbirth": "DateOfBirth",
    "socialsecuritynumber": "SocialSecurityNumber",
    "address": "Address",
    "city": "City",
    "state": "State",
    "zip": "Zip",
    "homephone": "HomePhone",
    "employername": "EmployerName",
    "employerphone": "EmployerPhone",
  };

  const insuranceMapping = {
    "carriername": "CarrierName",
    "subscribername": "SubscriberName",
    "policynumber": "PolicyNumber",
    "groupname": "GroupName",
    "groupnumber": "GroupNumber",
  };

  // For the spouse section, try both keys: "Spouse/SignificantOther" and "SpouseOrSignificantOther"
  const spouseDataRaw =
    patientData["Spouse/SignificantOther"] ||
    patientData.SpouseOrSignificantOther ||
    {};

  // Initialize state with normalized data.
  const [formData, setFormData] = useState({
    Patient: normalizeSection(patientData.Patient || {}, patientMapping),
    SpouseOrSignificantOther: normalizeSection(spouseDataRaw, spouseMapping),
    NextOfKin: normalizeSection(patientData.NextOfKin || {}, nextMapping),
    PrimaryInsurance: normalizeSection(patientData.PrimaryInsurance || {}, insuranceMapping),
  });

  // Update formData whenever patientData changes.
  useEffect(() => {
    const spouseDataRaw =
      patientData["Spouse/SignificantOther"] ||
      patientData.SpouseOrSignificantOther ||
      {};
    setFormData({
      Patient: normalizeSection(patientData.Patient || {}, patientMapping),
      SpouseOrSignificantOther: normalizeSection(spouseDataRaw, spouseMapping),
      NextOfKin: normalizeSection(patientData.NextOfKin || {}, nextMapping),
      PrimaryInsurance: normalizeSection(patientData.PrimaryInsurance || {}, insuranceMapping),
    });
  }, [patientData]);

  const handleChange = (section, field, value) => {
    setFormData((prev) => ({
      ...prev,
      [section]: {
        ...prev[section],
        [field]: value,
      },
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSave(formData);
  };

  return (
    <form onSubmit={handleSubmit} className="patient-form">
      <h2>Patient Information</h2>
      <div className="form-section">
        <label>
          Name:
          <input
            type="text"
            value={formData.Patient.Name || ""}
            onChange={(e) => handleChange("Patient", "Name", e.target.value)}
          />
        </label>
        <label>
          Date of Birth:
          {/* Here we assume the backend date is in ISO format or already normalized */}
          <input
            type="text"
            value={formData.Patient.DateOfBirth || ""}
            onChange={(e) => handleChange("Patient", "DateOfBirth", e.target.value)}
          />
        </label>
        <label>
          Social Security Number:
          <input
            type="text"
            value={formData.Patient.SocialSecurityNumber || ""}
            onChange={(e) =>
              handleChange("Patient", "SocialSecurityNumber", e.target.value)
            }
          />
        </label>
        <label>
          Address:
          <input
            type="text"
            value={formData.Patient.Address || ""}
            onChange={(e) => handleChange("Patient", "Address", e.target.value)}
          />
        </label>
        <label>
          City:
          <input
            type="text"
            value={formData.Patient.City || ""}
            onChange={(e) => handleChange("Patient", "City", e.target.value)}
          />
        </label>
        <label>
          State:
          <input
            type="text"
            value={formData.Patient.State || ""}
            onChange={(e) => handleChange("Patient", "State", e.target.value)}
          />
        </label>
        <label>
          Zip:
          <input
            type="text"
            value={formData.Patient.Zip || ""}
            onChange={(e) => handleChange("Patient", "Zip", e.target.value)}
          />
        </label>
        <label>
          Home Phone:
          <input
            type="text"
            value={formData.Patient.HomePhone || ""}
            onChange={(e) => handleChange("Patient", "HomePhone", e.target.value)}
          />
        </label>
        <label>
          Sex:
          <select
            value={formData.Patient.Sex || ""}
            onChange={(e) => handleChange("Patient", "Sex", e.target.value)}
          >
            <option value="">Select</option>
            <option value="Male">Male</option>
            <option value="Female">Female</option>
            <option value="Other">Other</option>
          </select>
        </label>
        <label>
          Race:
          <input
            type="text"
            value={formData.Patient.Race || ""}
            onChange={(e) => handleChange("Patient", "Race", e.target.value)}
          />
        </label>
        <label>
          Marital Status:
          <input
            type="text"
            value={formData.Patient.MaritalStatus || ""}
            onChange={(e) =>
              handleChange("Patient", "MaritalStatus", e.target.value)
            }
          />
        </label>
        <label>
          Religion:
          <input
            type="text"
            value={formData.Patient.Religion || ""}
            onChange={(e) =>
              handleChange("Patient", "Religion", e.target.value)
            }
          />
        </label>
        <label>
          Employer Name:
          <input
            type="text"
            value={formData.Patient.EmployerName || ""}
            onChange={(e) =>
              handleChange("Patient", "EmployerName", e.target.value)
            }
          />
        </label>
        <label>
          Employer Phone:
          <input
            type="text"
            value={formData.Patient.EmployerPhone || ""}
            onChange={(e) =>
              handleChange("Patient", "EmployerPhone", e.target.value)
            }
          />
        </label>
        <label>
          Physician:
          <input
            type="text"
            value={formData.Patient.FamilyPhysician || ""}
            onChange={(e) =>
              handleChange("Patient", "FamilyPhysician", e.target.value)
            }
          />
        </label>
        <label>
          Admitting Physician:
          <input
            type="text"
            value={formData.Patient.AdmittingPhysician || ""}
            onChange={(e) =>
              handleChange("Patient", "AdmittingPhysician", e.target.value)
            }
          />
        </label>
        <label>
          Delivery Due Date:
          <input
            type="text"
            value={formData.Patient.DeliveryDueDate || ""}
            onChange={(e) =>
              handleChange("Patient", "DeliveryDueDate", e.target.value)
            }
          />
        </label>
      </div>

      <h2>Spouse/Significant Other Information</h2>
      <div className="form-section">
        <label>
          Name:
          <input
            type="text"
            value={formData.SpouseOrSignificantOther.Name || ""}
            onChange={(e) =>
              handleChange("SpouseOrSignificantOther", "Name", e.target.value)
            }
          />
        </label>
        <label>
          Date of Birth:
          <input
            type="text"
            value={formData.SpouseOrSignificantOther.DateOfBirth || ""}
            onChange={(e) =>
              handleChange("SpouseOrSignificantOther", "DateOfBirth", e.target.value)
            }
          />
        </label>
        <label>
          Social Security Number:
          <input
            type="text"
            value={formData.SpouseOrSignificantOther.SocialSecurityNumber || ""}
            onChange={(e) =>
              handleChange("SpouseOrSignificantOther", "SocialSecurityNumber", e.target.value)
            }
          />
        </label>
        <label>
          Address:
          <input
            type="text"
            value={formData.SpouseOrSignificantOther.Address || ""}
            onChange={(e) =>
              handleChange("SpouseOrSignificantOther", "Address", e.target.value)
            }
          />
        </label>
        <label>
          City:
          <input
            type="text"
            value={formData.SpouseOrSignificantOther.City || ""}
            onChange={(e) =>
              handleChange("SpouseOrSignificantOther", "City", e.target.value)
            }
          />
        </label>
        <label>
          State:
          <input
            type="text"
            value={formData.SpouseOrSignificantOther.State || ""}
            onChange={(e) =>
              handleChange("SpouseOrSignificantOther", "State", e.target.value)
            }
          />
        </label>
        <label>
          Zip:
          <input
            type="text"
            value={formData.SpouseOrSignificantOther.Zip || ""}
            onChange={(e) =>
              handleChange("SpouseOrSignificantOther", "Zip", e.target.value)
            }
          />
        </label>
        <label>
          Home Phone:
          <input
            type="text"
            value={formData.SpouseOrSignificantOther.HomePhone || ""}
            onChange={(e) =>
              handleChange("SpouseOrSignificantOther", "HomePhone", e.target.value)
            }
          />
        </label>
        <label>
          Employer Name:
          <input
            type="text"
            value={formData.SpouseOrSignificantOther.EmployerName || ""}
            onChange={(e) =>
              handleChange("SpouseOrSignificantOther", "EmployerName", e.target.value)
            }
          />
        </label>
        <label>
          Employer Phone:
          <input
            type="text"
            value={formData.SpouseOrSignificantOther.EmployerPhone || ""}
            onChange={(e) =>
              handleChange("SpouseOrSignificantOther", "EmployerPhone", e.target.value)
            }
          />
        </label>
      </div>

      <h2>Next of Kin Information</h2>
      <div className="form-section">
        <label>
          Name:
          <input
            type="text"
            value={formData.NextOfKin.Name || ""}
            onChange={(e) =>
              handleChange("NextOfKin", "Name", e.target.value)
            }
          />
        </label>
        <label>
          Relationship to Patient:
          <input
            type="text"
            value={formData.NextOfKin.RelationshipToPatient || ""}
            onChange={(e) =>
              handleChange("NextOfKin", "RelationshipToPatient", e.target.value)
            }
          />
        </label>
        <label>
          Date of Birth:
          <input
            type="text"
            value={formData.NextOfKin.DateOfBirth || ""}
            onChange={(e) =>
              handleChange("NextOfKin", "DateOfBirth", e.target.value)
            }
          />
        </label>
        <label>
          Social Security Number:
          <input
            type="text"
            value={formData.NextOfKin.SocialSecurityNumber || ""}
            onChange={(e) =>
              handleChange("NextOfKin", "SocialSecurityNumber", e.target.value)
            }
          />
        </label>
        <label>
          Address:
          <input
            type="text"
            value={formData.NextOfKin.Address || ""}
            onChange={(e) =>
              handleChange("NextOfKin", "Address", e.target.value)
            }
          />
        </label>
        <label>
          City:
          <input
            type="text"
            value={formData.NextOfKin.City || ""}
            onChange={(e) =>
              handleChange("NextOfKin", "City", e.target.value)
            }
          />
        </label>
        <label>
          State:
          <input
            type="text"
            value={formData.NextOfKin.State || ""}
            onChange={(e) =>
              handleChange("NextOfKin", "State", e.target.value)
            }
          />
        </label>
        <label>
          Zip:
          <input
            type="text"
            value={formData.NextOfKin.Zip || ""}
            onChange={(e) =>
              handleChange("NextOfKin", "Zip", e.target.value)
            }
          />
        </label>
        <label>
          Home Phone:
          <input
            type="text"
            value={formData.NextOfKin.HomePhone || ""}
            onChange={(e) =>
              handleChange("NextOfKin", "HomePhone", e.target.value)
            }
          />
        </label>
        <label>
          Employer Name:
          <input
            type="text"
            value={formData.NextOfKin.EmployerName || ""}
            onChange={(e) =>
              handleChange("NextOfKin", "EmployerName", e.target.value)
            }
          />
        </label>
        <label>
          Employer Phone:
          <input
            type="text"
            value={formData.NextOfKin.EmployerPhone || ""}
            onChange={(e) =>
              handleChange("NextOfKin", "EmployerPhone", e.target.value)
            }
          />
        </label>
      </div>

      <h2>Primary Insurance Information</h2>
      <div className="form-section">
        <label>
          Carrier Name:
          <input
            type="text"
            value={formData.PrimaryInsurance.CarrierName || ""}
            onChange={(e) =>
              handleChange("PrimaryInsurance", "CarrierName", e.target.value)
            }
          />
        </label>
        <label>
          Subscriber Name:
          <input
            type="text"
            value={formData.PrimaryInsurance.SubscriberName || ""}
            onChange={(e) =>
              handleChange("PrimaryInsurance", "SubscriberName", e.target.value)
            }
          />
        </label>
        <label>
          Policy Number:
          <input
            type="text"
            value={formData.PrimaryInsurance.PolicyNumber || ""}
            onChange={(e) =>
              handleChange("PrimaryInsurance", "PolicyNumber", e.target.value)
            }
          />
        </label>
        <label>
          Group Name:
          <input
            type="text"
            value={formData.PrimaryInsurance.GroupName || ""}
            onChange={(e) =>
              handleChange("PrimaryInsurance", "GroupName", e.target.value)
            }
          />
        </label>
        <label>
          Group Number:
          <input
            type="text"
            value={formData.PrimaryInsurance.GroupNumber || ""}
            onChange={(e) =>
              handleChange("PrimaryInsurance", "GroupNumber", e.target.value)
            }
          />
        </label>
      </div>

      <button type="submit" className="save-button">
        Save Record
      </button>
    </form>
  );
};

export default PatientForm;
