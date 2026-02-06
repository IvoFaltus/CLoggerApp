import "./registerForm.css";

const RegisterForm = (props:any) => {
  return (
    <div className="regForm">
      <h1>Register</h1>

      <input type="text" placeholder="Username" />
      <input type="email" placeholder="Email" />
      <input type="password" placeholder="Password" />
      <input type="password" placeholder="Confirm Password" />

      <button className="primary">Create Account</button>
      <button className="link" onClick={() => props.setPage("login")}>
        Already have an account?
      </button>
    </div>
  );
};

export default RegisterForm;
