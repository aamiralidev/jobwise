import React from "react";

const SelectedFilters = ({ selectedFilters, removeFilter }) => {
  return (
    <div className="d-flex flex-wrap gap-2">
      {selectedFilters.map((filter) => (
        <div key={filter.id} className="border border-secondary ps-1 pe-1">
          <span>{filter.name}</span>
          <button
            onClick={() => removeFilter(filter)}
            className="border-0"
            style={{ background: "none" }}
          >
            &#x2715;
          </button>
        </div>
      ))}
    </div>
  );
};

export default SelectedFilters;
