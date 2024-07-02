import { useState } from "react";
import "./App.css";
import SearchPage from "./pages/SearchPage";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.min.js";
import {
  BrowserRouter,
  Routes,
  Route,
  Outlet,
  Navigate,
} from "react-router-dom";
import SolaraLogin from "./pages/Login/SolaraLogin";
import GreenLogin from "./pages/Login/GreenLogin";
import BlueLogin from "./pages/Login/BlueLogin";
import LeftLogin from "./pages/Login/LeftLogin";
import AddJobPage from "./pages/AddJobPage";

const PrivateRoutes = () => {
  const token = localStorage.getItem("access");
  return !token ? <Outlet /> : <Navigate to="/login" />;
};

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<LeftLogin />} />
        <Route path="/signup" element={<LeftLogin />} />
        <Route path="/" element={<PrivateRoutes />}>
          <Route path="/" element={<SearchPage />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
  // return <SearchPage />;
  // return <SolaraLogin />;
  // return <AddJobPage />;
}

export default App;
