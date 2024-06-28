import React, { useState } from "react";
import { IoLocationOutline, IoTimeOutline } from "react-icons/io5";
import { CgDollar } from "react-icons/cg";
import { CiCalendarDate } from "react-icons/ci";
import DOMPurify from "dompurify";

const timeSince = (datetime) => {
  // This function should convert datetime to a human-readable time since format.
  // For now, it just returns the datetime.
  return datetime;
};

const JobCard = ({ jobDetails }) => {
  const [expanded, setExpanded] = useState(false);

  const toggleExpand = () => {
    setExpanded(!expanded);
  };

  return (
    <div className="card mb-3 shadow-sm">
      <div className="card-body">
        <h5 className="card-title mb-1">{jobDetails.company_name}</h5>
        <h3 className="card-subtitle mb-3 text-primary">{jobDetails.title}</h3>
        <div className="d-flex flex-wrap gap-3 mb-3">
          <div className="d-flex gap-2 align-items-center">
            <IoLocationOutline size={18} />
            <div>{jobDetails.location}</div>
          </div>
          <div className="d-flex gap-2 align-items-center">
            <IoTimeOutline size={18} />
            <div>{jobDetails.commitment}</div>
          </div>
          <div className="d-flex gap-2 align-items-center">
            <CgDollar size={18} />
            <div>{jobDetails.salaryRange}</div>
          </div>
          <div className="d-flex gap-2 align-items-center">
            <CiCalendarDate size={18} />
            <div>{timeSince(jobDetails.date_posted)}</div>
          </div>
        </div>
        <div style={{ maxHeight: "calc(1.5em * 3)", overflow: "hidden" }}>
          <p
            className="card-text"
            dangerouslySetInnerHTML={{
              __html: DOMPurify.sanitize(jobDetails.job_description),
            }}
          />
          <button
            className={`btn btn-link position-absolute bottom-0 end-0 m-2 ${
              !expanded ? "blurry-background" : ""
            }`}
            onClick={toggleExpand}
            style={{ textDecoration: "none" }}
          >
            {expanded ? "Show less" : "Show more"}
          </button>
        </div>
      </div>
    </div>
  );
};

export default JobCard;
