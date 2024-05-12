import React, { useState } from "react";
import { Multiselect as MSelect } from "multiselect-react-dropdown";

const MultiSelect = ({
  options,
  addFilter,
  placeholder,
  removeFilter,
}) => {
  const chip_style = {
    chips: {
      display: "none",
    },
    searchBox: {
      borderRadius: "0",
    },
    optionContainer: {
      borderRadius: "0",
    },
    option: {
      accentColor: "blue",
    },
  };
  const handleSelect = (_, selectedItem) => {
    addFilter(selectedItem);
  };
  const handleRemove = (_, removedItem) => {
    removeFilter(removedItem);
  };
  return (
    <div style={{ minWidth: "200px", maxWidth: "160px" }}>
      <MSelect
        options={options}
        placeholder={placeholder}
        selectedValues={[]}
        onSelect={handleSelect}
        onRemove={handleRemove}
        showCheckbox={true}
        displayValue="name"
        avoidHighlightFirstOption={true}
        showArrow={true}
        disablePreSelectedValues={true}
        style={chip_style}
      />
    </div>
  );
};

export default MultiSelect;
