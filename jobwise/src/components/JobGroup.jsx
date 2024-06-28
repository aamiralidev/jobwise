import React from "react";
import JobCard from "./JobCard";

const JobGroup = ({ jobs = [] }) => {
  console.log(jobs)
  return (
    <div className="d-flex flex-column gap-4 mt-3">
      {!jobs.length && <div>No jobs found</div>}
      {jobs.map((job) => (
        <JobCard key={job.id} jobDetails={job} />
      ))}
    </div>
  );
};

export default JobGroup;
