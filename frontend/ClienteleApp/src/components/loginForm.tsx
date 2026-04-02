import { Navigate } from "react-router-dom";
import "../styles/loginForm.css";


import { useNavigate } from "react-router-dom";
import { useState } from "react";

type loginReponse = | {"msg":string} | {"token":string}

const LoginForm = (props:any) => {

  const navigate = useNavigate()
  const [username,setUsername] = useState("")
    const [password,setPasswd]= useState("")
  const sendData =async():Promise<loginReponse>=>{
    
    
    const res = await fetch('http://localhost:5000/login_check',{
      method: "POST",
      headers:{
        "Content-Type":"application/json",
      },
      credentials: "include",  
      body:JSON.stringify({username,password})

    })
    const data = await res.json()

    return data
  }
  
  const tryLogin = async()=>{
    const data:object = await sendData()

    if("token" in data){
      navigate('/deepweb/')
      
    }else{
       
    }
  }



  const login = () =>{navigate("/deepweb")}
  return (
    <div className="loginForm">
      <h1>Login</h1>

      
      <input type="username" value={username} className="username-input" onChange={(e)=>setUsername(e.target.value)} placeholder="username" />
      <input type="password" value={password} className="password-input" onChange={(e)=>setPasswd(e.target.value)} placeholder="Password" />

      <button className="primary" onClick={tryLogin} >Login</button>
      <button className="link" onClick={() => navigate("/register")}>
        Create account
      </button>
    </div>
  );
};

export default LoginForm;


