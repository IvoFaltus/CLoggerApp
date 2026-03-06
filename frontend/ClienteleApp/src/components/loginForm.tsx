import { Navigate } from "react-router-dom";
import "./loginForm.css";


import { useNavigate } from "react-router-dom";


const LoginForm = (props:any) => {

  const navigate = useNavigate()

  const login = () =>{navigate("/deepweb")}
  return (
    <div className="loginForm">
      <h1>Login</h1>

      
      <input type="email" placeholder="Email" />
      <input type="password" placeholder="Password" />

      <button className="primary" onClick={()=>login()} >Login</button>
      <button className="link" onClick={() => navigate("/register")}>
        Create account
      </button>
    </div>
  );
};

export default LoginForm;
