import React from "react";
import { IoLocationOutline } from "react-icons/io5";
import { IoTimeOutline } from "react-icons/io5";
import { CgDollar } from "react-icons/cg";
import { CiCalendarDate } from "react-icons/ci";

const timeSince = (datetime) => {
  return datetime;
};

const JobCard = ({ jobDetails }) => {
  return (
    <div className="d-flex bg-white p-3">
      <div className="" style={{ width: "10%" }}></div>
      <div className="d-flex flex-column gap-3" style={{ width: "90%" }}>
        <div>{jobDetails.companyName}</div>
        <h3>{jobDetails.positionTitle}</h3>
        <div className="d-flex justify-content-between">
          <div className="d-flex gap-2 align-items-center">
            <IoLocationOutline size={18} />
            <div>{jobDetails.location}</div>
          </div>
          <div className="d-flex gap-2 align-items-center">
            <IoTimeOutline size={18} />
            <div>{jobDetails.jobTime}</div>
          </div>
          <div className="d-flex gap-2 align-items-center">
            <CgDollar size={18} />
            <div>{jobDetails.salaryRange}</div>
          </div>
          <div className="d-flex gap-2 align-items-center">
            <CiCalendarDate size={18} />
            <div>{timeSince(jobDetails.postedAt)}</div>
          </div>
        </div>
        <div>{jobDetails.description}</div>
      </div>
    </div>
  );
};

export default JobCard;
