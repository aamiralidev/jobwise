import React from "react";
import Filters from "./Filters";
import JobGroup from "./JobGroup";
import Sidebar from "./Sidebar";
import { useState } from "react";
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
    <div
      className="d-flex m-5 justify-content-around"
      style={{ backgroundColor: "#F5F5F5" }}
    >
      <div
        style={{ minWidth: "250px" }}
        className="bg-white p-4 d-flex flex-column gap-4 h-100"
      >
        <h1>Filters</h1>
        <Filters addFilter={addFilter} removeFilter={removeFilter} />
      </div>
      <div className="ms-5 me-5" style={{ width: "60%" }}>
        <h1>3577 Jobs</h1>
        <SelectedFilters
          selectedFilters={selectedFilters}
          removeFilter={removeFilter}
        />
        <JobGroup />
      </div>
      <div style={{ minWidth: "250px" }}>
        <Sidebar />
      </div>
    </div>
  );
};

export default Content;
