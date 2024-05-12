import React from "react";
import JobCard from "./JobCard";

const JobGroup = () => {
  const jobs = [
    {
      id: 1,
      logoUrl: "AltText",
      companyName: "Linear Company",
      positionTitle: "Software Engineer",
      location: "Brussels",
      jobTime: "Full-Time",
      salaryRange: "50-55k",
      postedAt: "datetime",
    },
    {
      id: 2,
      logoUrl: "AltText",
      companyName: "Linear Company",
      positionTitle: "Software Engineer",
      location: "Brussels",
      jobTime: "Full-Time",
      salaryRange: "50-55k",
      postedAt: "datetime",
    },
    {
      id: 3,
      logoUrl: "AltText",
      companyName: "Linear Company",
      positionTitle: "Software Engineer",
      location: "Brussels",
      jobTime: "Full-Time",
      salaryRange: "50-55k",
      postedAt: "datetime",
    },
    {
      id: 4,
      logoUrl: "AltText",
      companyName: "Linear Company",
      positionTitle: "Software Engineer",
      location: "Brussels",
      jobTime: "Full-Time",
      salaryRange: "50-55k",
      postedAt: "datetime",
    },
    {
      id: 5,
      logoUrl: "AltText",
      companyName: "Linear Company",
      positionTitle: "Software Engineer",
      location: "Brussels",
      jobTime: "Full-Time",
      salaryRange: "50-55k",
      postedAt: "datetime",
    },
    {
      id: 6,
      logoUrl: "AltText",
      companyName: "Linear Company",
      positionTitle: "Software Engineer",
      location: "Brussels",
      jobTime: "Full-Time",
      salaryRange: "50-55k",
      postedAt: "datetime",
    },
  ];

  return (
    <div className="d-flex flex-column gap-4 mt-3">
      {jobs.map((job) => (
        <JobCard key={job.id} jobDetails={job} />
      ))}
    </div>
  );
};

export default JobGroup;
