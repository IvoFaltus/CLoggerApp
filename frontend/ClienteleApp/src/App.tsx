
import Deepweb from "./pages/deepweb";
import Login from "./pages/login";
import Register from "./pages/register";
import Protect from "./components/Protect";
import NotProtect from "./components/notProtect";
import { useState } from "react";
import { BrowserRouter,Routes,Route } from "react-router-dom";

function App() {
  

  return <BrowserRouter>

  <Routes>
<Route path="/login" element={ <NotProtect component={Login} />} />
<Route path="/register" element={<NotProtect component={Register} />} />
<Route path="/deepweb" element={<Protect component={Deepweb} />} />
  </Routes>
</BrowserRouter>
}

export default App;
