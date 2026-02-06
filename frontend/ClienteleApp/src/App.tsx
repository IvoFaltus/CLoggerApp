
import Login from "./components/login";
import Register from "./components/register";
import { useState } from "react";


function App() {
  const[page,setPage] = useState("login")

  return <>
    {page === "login" && <Login setPage={setPage} />}
    {page ==="register" && <Register setPage={setPage}/>}
    
  </>
}

export default App;
