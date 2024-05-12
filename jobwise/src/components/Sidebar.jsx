import React from "react";

const Sidebar = () => {
  return (
    <div className="d-flex flex-column gap-5">
      <div className="d-flex flex-column gap-3 bg-white p-4">
        <div>
          <h5>Email me for Jobs</h5>
        </div>
        <div>
          <input
            placeholder="name@email.com"
            type="email"
            className="form-control"
          />
        </div>
        <div className="d-grid">
          <button className="btn btn-primary">Subscribe</button>
        </div>
      </div>
      <div className="d-flex flex-column gap-3 bg-white p-4">
        <div>
          <h5>Get Noticed Faster</h5>
        </div>
        <div className="d-grid">
          <button className="btn btn-primary">Upload Your Resume</button>
        </div>
      </div>
    </div>
  );
};

export default Sidebar;
