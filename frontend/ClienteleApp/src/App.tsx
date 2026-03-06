
import Deepweb from "./components/deepweb";
import Login from "./components/login";
import Register from "./components/register";
import { useState } from "react";
import { BrowserRouter,Routes,Route } from "react-router-dom";

function App() {
  

  return <BrowserRouter>

  <Routes>
<Route path="/login" element={ <Login/>} />
<Route path="/register" element={<Register />} />
<Route path="/deepweb" element={<Deepweb />} />
  </Routes>
</BrowserRouter>
}

export default App;
