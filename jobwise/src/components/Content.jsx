import React, { useState, useEffect } from "react";
import Filters from "./Filters";
import JobGroup from "./JobGroup";
import Sidebar from "./Sidebar";
import SelectedFilters from "./SelectedFilters";
import { getJobs } from "../api/JobsApi";
import useWindowDimensions from "../hooks/dimension";
import { LiaFilterSolid } from "react-icons/lia";
import { RxCross2 } from "react-icons/rx";

const Content = () => {
  const { height, width } = useWindowDimensions();
  const [expanded, setExpanded] = useState(false);
  const widthThreshold = 900;
  const toggleExpand = () => setExpanded(!expanded);

  const [selectedFilters, setSelectedFilters] = useState([]);
  const [jobs, setJobs] = useState([]);

  const addFilter = (filter) => {
    setSelectedFilters([...selectedFilters, filter]);
  };

  const updateJobs = () => {
    getJobs()
      .then((response) => {
        setJobs(response.data["results"]);
      })
      .catch((error) => console.error("Error fetching jobs:", error));
  };

  const removeFilter = (filter) => {
    const index = selectedFilters.indexOf(filter);
    setSelectedFilters(selectedFilters.toSpliced(index, 1));
  };

  useEffect(() => {
    updateJobs();
  }, []);

  return (
    <div
      className="container-fluid pt-5 px-3 px-md-4"
      style={{ maxWidth: "1440px" }}
    >
      <div
        className="d-flex"
        style={{ backgroundColor: "#F5F5F5", position: "relative" }}
      >
        {(width > widthThreshold || expanded) && (
          <div
            className="d-flex flex-column gap-5"
            style={
              width <= widthThreshold && expanded
                ? {
                    position: "absolute",
                    zIndex: 10,
                    backgroundColor: "#fff",
                    top: -50,
                    left: 0,
                    overflowY: "auto",
                    padding: "20px",
                    boxShadow: "0 8px 8px rgba(0, 0, 0, 0.1)",
                  }
                : {}
            }
          >
            <div className="bg-white p-4 d-flex flex-column gap-4">
              <div className="d-flex">
                <h1>Filters</h1>
                <div
                  className="ms-2 pb-2"
                  style={{ position: "relative", top: "-6px" }}
                >
                  {width <= widthThreshold && (
                    <button
                      className="border-0 bg-transparent p-0"
                      style={{ cursor: "pointer" }}
                      onClick={toggleExpand}
                    >
                      <RxCross2 size={50} />
                    </button>
                  )}
                </div>
              </div>
              <Filters addFilter={addFilter} removeFilter={removeFilter} />
            </div>
            <div>
              <Sidebar />
            </div>
          </div>
        )}

        <div
          className={width > widthThreshold && "ms-5"}
          style={{ minWidth: "400px" }}
        >
          <div className="d-flex">
            <h1>3577 Jobs</h1>
            <div
              className="ms-2 pb-2"
              style={{ position: "relative", top: "-6px" }}
            >
              {width <= widthThreshold && (
                <button
                  className="border-0 bg-transparent p-0"
                  style={{ cursor: "pointer" }}
                  onClick={toggleExpand}
                >
                  <LiaFilterSolid size={50} />
                </button>
              )}
            </div>
          </div>
          <div className="mt-auto" style={{ width: "90%" }}>
            <SelectedFilters
              selectedFilters={selectedFilters}
              removeFilter={removeFilter}
            />
          </div>
          <JobGroup jobs={jobs} />
        </div>
      </div>
    </div>
  );
};

export default Content;
