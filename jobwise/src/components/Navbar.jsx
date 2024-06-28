import React from "react";
import useWindowDimensions from "../hooks/dimension";

const Navbar = () => {
  const { height, width } = useWindowDimensions();

  return (
    <nav className="navbar navbar-expand-md navbar-light bg-white shadow-sm">
      <div
        className="container-fluid p-3 p-md-4"
        style={{ maxWidth: "1440px" }}
      >
        <a className="navbar-brand" href="#">
          JobWise
        </a>
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          <ul className="navbar-nav me-auto">
            <li className="nav-item">
              <a className="nav-link" aria-current="page" href="#">
                Start a Search
              </a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="#">
                Jobs List
              </a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="#">
                Salary Estimate
              </a>
            </li>
            <li className="nav-item">
              <a className="nav-link" href="#">
                Pricing
              </a>
            </li>
          </ul>
          <div
            className={`${
              width < 800
                ? "d-flex flex-column gap-3 align-items-start mt-4"
                : "d-flex align-items-center gap-3"
            }`}
          >
            <button className="btn btn-outline-primary">Log In</button>
            <button className="btn btn-primary">Sign Up</button>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
