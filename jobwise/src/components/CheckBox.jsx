import React, { useState } from "react";

const CheckBox = ({ label, setSelected }) => {
  const [isChecked, setIsChecked] = useState(false);
  const handleCheckboxChange = () => {
    const newCheckedState = !isChecked;
    setIsChecked(newCheckedState);
    // Call the onChange callback if provided
    if (setSelected) {
      setSelected(newCheckedState);
    }
  };
  return (
    <div>
      <label>
        <input
          type="checkbox"
          checked={isChecked}
          onChange={handleCheckboxChange}
          style={{
            marginRight: "8px",
            accentColor: "blue",
            transform: "scale(1.2)",
          }}
        />
        {label}
      </label>
    </div>
  );
};

export default CheckBox;
