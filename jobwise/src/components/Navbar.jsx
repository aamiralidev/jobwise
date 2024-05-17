import React from "react";

const Navbar = () => {
  return (
    <nav className="navbar navbar-expand-lg fw-bold bg-white ps-5 pe-3">
      <div className="container-fluid">
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
          <div className="d-flex justify-content-center w-75">
            <ul className="navbar-nav gap-4 ps-5 ms-5">
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
          </div>
          <div className="d-flex gap-3">
            <button className="btn btn-outline-primary">Log In</button>
            <button className="btn btn-primary">Sign Up</button>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
