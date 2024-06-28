import React, { useState, useEffect } from "react";
import Filters from "./Filters";
import JobGroup from "./JobGroup";
import Sidebar from "./Sidebar";
import SelectedFilters from "./SelectedFilters";
import { getJobs } from "../api/JobsApi";
import useWindowDimensions from "../hooks/dimension";

const Content = () => {
  const { height, width } = useWindowDimensions();

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
      <div className="d-flex" style={{ backgroundColor: "#F5F5F5" }}>
        <div className="d-flex flex-column gap-5">
          <div className="bg-white p-4 d-flex flex-column gap-4">
            <h1>Filters</h1>
            <Filters addFilter={addFilter} removeFilter={removeFilter} />
          </div>
          <div>
            <Sidebar />
          </div>
        </div>

        <div className="ms-5 me-5" style={{ minWidth: "400px" }}>
          <h1>3577 Jobs</h1>
          <SelectedFilters
            selectedFilters={selectedFilters}
            removeFilter={removeFilter}
          />
          <JobGroup jobs={jobs} />
        </div>
      </div>
    </div>
  );
};

export default Content;
