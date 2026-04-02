import type { ComponentType } from "react";
import Register from "../pages/login";
import { useEffect, useState } from "react";
import Deepweb from "../pages/deepweb";
import { useNavigate } from "react-router-dom";
type LoginProps = {
  component: ComponentType;
};

const Protect = ({ component: Component }: LoginProps) => {
  const [auth, setAuth] = useState<boolean | null>(null);

  const navigate = useNavigate()
  useEffect(() => {
  fetch("http://localhost:5000/verify_token", {
    credentials: "include"
  })
    .then(res => {
      if (!res.ok) {
        setAuth(false)
        return null
      }
      return res.json()
    })
    .then(data => {
      if (!data) return

      if (data.msg === "success") {
        setAuth(true)
      } else {
        setAuth(false)
      }
    })
    .catch(() => {
      setAuth(false)
    })
}, [])




  return (
    <>
      {auth == null && <><h1>Loading....</h1></>}
      {auth && <Component />}
      {!auth && navigate("/login")}
    </>
  );
}
export default Protect
