import { useNavigate } from "react-router-dom";
import "./registerForm.css";

import { useState } from "react";
const RegisterForm = (props:any) => {

const navigate = useNavigate()

const [num,setNumber]=useState(0)

  return (
    <div className="regForm">
      <h1>Register</h1>

      <input type="text" placeholder="Username" />
      <input type="email" placeholder="Email" />
      <input type="password" placeholder="Password" />
      <input type="password" placeholder="Confirm Password" />

      <button className="primary">Create Account</button>
       <button className="link" onClick={() => navigate("/login")}> 
        

        Already have an account?
      </button>
      
    </div>
  );
};

export default RegisterForm;
