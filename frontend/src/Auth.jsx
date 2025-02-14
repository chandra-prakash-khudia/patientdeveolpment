// Auth.jsx
import React, { useState } from "react";
import Login from "./Login.jsx";
import Signup from "./SignUp.jsx";
import "./Auth.css";

function Auth({ onLogin }) {
  const [isLogin, setIsLogin] = useState(true);

  return (
    <div className="auth-container">
      <div className="auth-toggle">
        <button
          className={isLogin ? "active" : ""}
          onClick={() => setIsLogin(true)}
        >
          Login
        </button>
        <button
          className={!isLogin ? "active" : ""}
          onClick={() => setIsLogin(false)}
        >
          Sign Up
        </button>
      </div>
      {isLogin ? <Login onLogin={onLogin} /> : <Signup onLogin={onLogin} />}
    </div>
  );
}

export default Auth;
