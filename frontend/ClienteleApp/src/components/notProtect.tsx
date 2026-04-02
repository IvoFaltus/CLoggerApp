
import { useEffect, type ComponentType } from "react";
import { useNavigate } from "react-router-dom";
type Prop = {


    "component":ComponentType
}


const notProtect = ({"component":Component}:Prop)=>{

    useEffect(()=>{
fetch("http://localhost:5000/delete_session", {
    method:"DELETE",
    credentials: "include"
  })


    },[])



    return <>  
    {<Component></Component>}
    </>

    
}







export default notProtect;