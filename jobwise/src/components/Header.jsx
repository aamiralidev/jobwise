import React from "react";
import Navbar from "./Navbar";
import { CiSearch } from "react-icons/ci";
import { IoLocationOutline } from "react-icons/io5";

const Header = () => {
  return (
    <>
      <Navbar />
      <div
        className="container-fluid p-3 p-md-4"
        style={{ maxWidth: "1440px" }}
      >
        <div className="bg-white px-4 py-5">
          <div className="text-start">
            <h1 className="mb-2 fw-bold display-4">
              Find your <span className="text-primary">new job</span> today
            </h1>
            <p className="lead">
              Thousands of jobs in the computer, engineering, and technology
              sectors are waiting for you.
            </p>
          </div>
          <div className="row mt-4 g-2">
            <div className="col-12 col-md-5">
              <div className="input-group">
                <span className="input-group-text bg-white border border-dark">
                  <CiSearch />
                </span>
                <input
                  type="text"
                  className="form-control border border-primary"
                  placeholder="What are you looking for?"
                  aria-label="job"
                  aria-describedby="basic-addon1"
                />
              </div>
            </div>
            <div className="col-12 col-md-5">
              <div className="input-group">
                <span className="input-group-text bg-white border border-dark">
                  <IoLocationOutline />
                </span>
                <input
                  type="text"
                  className="form-control border border-primary"
                  placeholder="Location"
                  aria-label="location"
                  aria-describedby="basic-addon2"
                />
              </div>
            </div>
            <div className="col-12 col-md-2">
              <button className="btn btn-primary w-100" type="button">
                Search Job
              </button>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default Header;
