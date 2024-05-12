import React from "react";
import Navbar from "./Navbar";
import { CiSearch } from "react-icons/ci";
import { IoLocationOutline } from "react-icons/io5";

const Header = () => {
  return (
    <>
      <Navbar />
      <div className="container-fluid bg-white header-background">
        <div className="p-2 ps-5 pb-5">
          <div className="d-flex flex-column mt-5 pt-5">
            <div className="">
              <h1 className="mb-2 fw-bold fst-6" style={{ fontSize: "5em" }}>
                Find your <span className="text-primary">new job</span> today
              </h1>
              <p style={{ fontSize: "1.5em" }}>
                Thousands of jobs in the computer, engineering and technology
                sectors are waiting for you.
              </p>
            </div>
            <div className="input-group d-flex justify-content-between mt-4 ">
              <div className="" style={{ width: "45%" }}>
                <div
                  className="input-group border"
                  style={{ height: "5rem", width: "100%" }}
                >
                  <span
                    className="input-group-text bg-white border-0"
                    id="basic-addon1"
                  >
                    <CiSearch />
                  </span>
                  <input
                    type="text"
                    className="form-control border-0 w-50 shadow-none bg-white"
                    placeholder="Whar are you looking for ?"
                    aria-label="job"
                    aria-describedby="basic-addon1"
                    style={{ outline: "none" }}
                  />
                </div>
              </div>
              <div className="group-outline" style={{ width: "45%" }}>
                <div
                  className="input-group border"
                  style={{ height: "5rem", width: "100%" }}
                >
                  <span
                    className="input-group-text bg-white border-0"
                    id="basic-addon1"
                  >
                    <CiSearch />
                  </span>
                  <input
                    type="text"
                    className="form-control border-0 shadow-none bg-white"
                    placeholder="Location "
                    aria-label="location"
                    aria-describedby="basic-addon1"
                  />
                </div>
              </div>
              <button
                className="btn btn-primary"
                type="button"
                style={{ width: "10%" }}
              >
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
