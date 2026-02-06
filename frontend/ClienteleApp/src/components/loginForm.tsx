import "./loginForm.css";

const LoginForm = (props:any) => {
  return (
    <div className="loginForm">
      <h1>Login</h1>

      <input type="email" placeholder="Email" />
      <input type="password" placeholder="Password" />

      <button className="primary">Login</button>
      <button className="link" onClick={() => props.setPage("register")}>
        Create account
      </button>
    </div>
  );
};

export default LoginForm;
