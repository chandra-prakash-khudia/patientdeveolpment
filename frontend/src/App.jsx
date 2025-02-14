// App.jsx
import React, { useState, useEffect } from "react";
import "./App.css";
import PatientForm from "./patientinfo.jsx";
import Auth from "./Auth.jsx";

function App() {
  const [token, setToken] = useState(localStorage.getItem("access_token") || "");
  const [file, setFile] = useState(null);
  const [patientData, setPatientData] = useState(null);
  const [doctorQuery, setDoctorQuery] = useState("");
  const [chatHistory, setChatHistory] = useState([]);
  const [isProcessing, setIsProcessing] = useState(false);

  useEffect(() => {
    if (token) {
      localStorage.setItem("access_token", token);
    } else {
      localStorage.removeItem("access_token");
    }
  }, [token]);

  const authHeaders = token ? { Authorization: `Bearer ${token}` } : {};

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) return;
    setIsProcessing(true);
    const formData = new FormData();
    formData.append("file", file);
    try {
      const res = await fetch("http://localhost:8000/upload", {
        method: "POST",
        headers: { ...authHeaders },
        body: formData,
      });
      if (!res.ok) throw new Error("Upload failed");
      const data = await res.json();
      console.log(data);
      setPatientData(data);
    } catch (error) {
      console.error("Upload Error:", error);
      alert("Error uploading file");
    }
    setIsProcessing(false);
  };

  const handleSave = async (updatedData) => {
    setIsProcessing(true);
    try {
      const res = await fetch("http://localhost:8000/save", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          ...authHeaders,
        },
        body: JSON.stringify(updatedData),
      });
      if (!res.ok) throw new Error("Save failed");
      const result = await res.json();
      alert(result.message);
      // Clear the patientData state to remove the form from the UI after successful submission
      setPatientData(null);
    } catch (error) {
      console.error("Save Error:", error);
      alert("Error saving record");
    }
    setIsProcessing(false);
  };

  const handleSearch = async () => {
    if (!doctorQuery) return;
    setIsProcessing(true);
    try {
      const res = await fetch(
        `http://localhost:8000/search?doctor_query=${encodeURIComponent(doctorQuery)}`,
        { headers: { ...authHeaders } }
      );
      if (!res.ok) throw new Error("Search failed");
      const result = await res.json();
      const responseText = result.final_response || result.message;
      // Append the new search to the chat history
      setChatHistory((prevHistory) => [
        ...prevHistory,
        { query: doctorQuery, response: responseText },
      ]);
      // Clear the input field if desired
      setDoctorQuery("");
    } catch (error) {
      console.error("Search Error:", error);
      alert("Error searching record");
    }
    setIsProcessing(false);
  };

  if (!token) {
    return (
      <div className="container">
        <Auth onLogin={setToken} />
      </div>
    );
  }

  return (
    <div className="container">
      <header>
        <h1>Medical Form Processor</h1>
      </header>

      {isProcessing && (
        <div className="overlay">
          <div className="spinner"></div>
          <p>Processing...</p>
        </div>
      )}

      <section className="upload-section">
        <h2>Upload Patient Form</h2>
        <input
          type="file"
          accept="image/jpeg,image/jpg"
          onChange={handleFileChange}
        />
        <button onClick={handleUpload}>Upload</button>
      </section>

      {patientData && (
        <section className="patient-form-section">
          <h2>Patient Data</h2>
          <PatientForm patientData={patientData} onSave={handleSave} />
        </section>
      )}

      <section className="search-section">
        <h2>Search Patient Record</h2>
        <input
          type="text"
          placeholder="Enter doctor's query..."
          value={doctorQuery}
          onChange={(e) => setDoctorQuery(e.target.value)}
        />
        <button onClick={handleSearch}>Search</button>

        {chatHistory.length > 0 && (
          <div className="chat-history">
            <h3>Chat History</h3>
            {chatHistory.map((chat, index) => (
              <div key={index} className="chat-message">
                <div className="doctor-query">
                  <strong>Doctor:</strong> {chat.query}
                </div>
                <div className="final-response">
                  <strong>Response:</strong> {chat.response}
                </div>
              </div>
            ))}
          </div>
        )}
      </section>
    </div>
  );
}

export default App;
