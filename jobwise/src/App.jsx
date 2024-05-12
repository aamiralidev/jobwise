import { useState } from "react";
import "./App.css";
import SearchPage from "./pages/SearchPage";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.min.js";
import SolaraLogin from "./pages/Login/SolaraLogin";
import GreenLogin from "./pages/Login/GreenLogin";
import BlueLogin from "./pages/Login/BlueLogin";
import LeftLogin from "./pages/Login/LeftLogin";
import AddJobPage from "./pages/AddJobPage";

function App() {
  return <SearchPage />;
  // return <SolaraLogin />;
  // return <AddJobPage />;
}

export default App;
