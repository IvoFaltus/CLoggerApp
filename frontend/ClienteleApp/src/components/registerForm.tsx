import { useNavigate } from "react-router-dom";
import "../styles/registerForm.css";

import { useState } from "react";
const RegisterForm = (props: any) => {


  const navigate = useNavigate()
  

  const [username, setUsername] = useState("")
  const [name, setName] = useState("")
  const [lastname, setLastname] = useState("")
  const [password, setPassword] = useState("")
  const [password2, setPassword2] = useState("")
const [error, setError] = useState("");


  const sendData = async () => {
    if (password != password2) {
      setError("Passwords do not match")
      
      setTimeout(() => { setError("") }, 3000)
      return
    }
    try {
      const res = await fetch("http://localhost:5000/create_user", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          "username": username,
          "name": name,
          "lastname": lastname,
          "password": password
        })

      })
      const data = await res.json()

      if (data.msg === "success") {
  navigate("/login")
} else {
  switch (data.msg) {
    case "name_error":
      setError("Name must start with capital letter and be 2–50 chars")
      break
    case "lastname_error":
      setError("Last name must start with capital letter and be 2–50 chars")
      break
    case "username_format_error":
      setError("Username must be 4–20 chars (letters, numbers, _)")
      break
    case "password_error":
      setError("Password must be 8–50 chars, include letter and number")
      break
    case "username_exists_error":
      setError("Username already exists")
      break
    default:
      setError("Unknown error")
  }

  setTimeout(() => setError(""), 3000)
}


 } catch (e) {
  setError("Server error")
  setTimeout(() => setError(""), 3000)
}

  }

  return (
    <div className="regForm">

      <form action="" onSubmit={e => { e.preventDefault(); sendData() }}>
        <h1>Register</h1>

        <input
          value={username}
          onChange={e => setUsername(e.target.value)}
          type="text"
          placeholder="Username"
          required
        />

        <input
          value={name}
          onChange={e => setName(e.target.value)}
          type="text"
          placeholder="Name"
          required
        />

        <input
          value={lastname}
          onChange={e => setLastname(e.target.value)}
          type="text"
          placeholder="Last Name"
          required
        />

        <input
          value={password}
          onChange={e => setPassword(e.target.value)}
          type="password"
          placeholder="Password"
          required
        />

        <input
          value={password2}
          onChange={e => setPassword2(e.target.value)}
          type="password"
          placeholder="Confirm Password"
          required
        />

        <button className="primary" type='submit' >Create Account</button>
        <button className="link" type='button'onClick={() => navigate("/login")}>


          Already have an account?
        </button>

      </form>


      {error && <h1>{error}</h1>}
    </div>
  );
};

export default RegisterForm;
