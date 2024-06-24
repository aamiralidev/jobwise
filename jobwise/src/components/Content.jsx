import React, { useState } from "react";
import Filters from "./Filters";
import JobGroup from "./JobGroup";
import Sidebar from "./Sidebar";
import SelectedFilters from "./SelectedFilters";

const Content = () => {
  const [selectedFilters, setSelectedFilters] = useState([]);

  const addFilter = (filter) => {
    setSelectedFilters([...selectedFilters, filter]);
  };

  const removeFilter = (filter) => {
    const index = selectedFilters.indexOf(filter);
    setSelectedFilters(selectedFilters.toSpliced(index, 1));
  };

  return (
    <div className="container-fluid pt-5 px-3 px-md-4" style={{ maxWidth: "1440px" }}>
      <div className="row" style={{ backgroundColor: "#F5F5F5" }}>
        <div className="col-12 col-md-3 mb-4 mb-md-0" style={{ minWidth: "250px" }}>
          <div className="bg-white p-4 d-flex flex-column gap-4 h-100">
            <h1>Filters</h1>
            <Filters addFilter={addFilter} removeFilter={removeFilter} />
          </div>
        </div>
        <div className="col-12 col-md-6 mb-4 mb-md-0">
          <div className="ms-md-5 me-md-5">
            <h1>3577 Jobs</h1>
            <SelectedFilters selectedFilters={selectedFilters} removeFilter={removeFilter} />
            <JobGroup />
          </div>
        </div>
        <div className="col-12 col-md-3" style={{ minWidth: "250px" }}>
          <Sidebar />
        </div>
      </div>
    </div>
  );
};

export default Content;
