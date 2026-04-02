import RegisterForm from "../components/registerForm"
import "../styles/register.css"


const Register = (props: any) => {
    return <div className="regPage">
    
    <RegisterForm setPage={props.setPage}/>
    
    </div>
}

export default Register