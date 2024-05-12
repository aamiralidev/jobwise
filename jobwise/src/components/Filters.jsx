import React, { useState } from "react";
import MultiSelect from "../components/MultiSelect";
import CheckBox from "../components/CheckBox";
import "../index.css";

const Filters = ({ addFilter, removeFilter }) => {
  const [selectedExperiances, setSelectedExperiances] = useState([]);
  const [selectedWorkplaces, setSelectedWorkplaces] = useState([]);
  const [selectedCommitment, setSelectedCommitment] = useState([]);
  const [selectedContract, setSelectedContract] = useState([]);
  const [selectedDegree, setSelectedDegree] = useState([]);
  const [selectedPublishDate, setSelectedPublishDate] = useState([]);
  const [visaSponsorship, setVisaSponsorship] = useState(false);
  const [relocationSupport, setRelocationSupport] = useState(false);
  const [remoteFromAnywhere, setRemoteFromAnywhere] = useState(false);

  const experianceOptions = [
    { id: "internship", name: "Internship" },
    { id: "apprenticeship", name: "Apprenticeship" },
    { id: "freshgrad", name: "FreshGrad" },
    { id: "associate", name: "Entry & Associate" },
    { id: "mid", name: "Mid-Level" },
    { id: "senior", name: "Senior Level" },
    { id: "staff", name: "Staff Level" },
    { id: "director", name: "Director" },
    { id: "executive", name: "Executive" },
  ];

  const workplaceOptions = [
    { id: "remote", name: "Remote" },
    { id: "onsite", name: "On-Site" },
    { id: "hybrid", name: "Hybrid" },
  ];

  const commitmentOptions = [
    { id: "fulltime", name: "Full-Time" },
    { id: "parttime", name: "Part-Time" },
  ];

  const contractOptions = [
    { id: "temporary", name: "Temporary" },
    { id: "permanent", name: "Permanent" },
  ];

  const degreeOptions = [
    { id: "bachelor", name: "Bachelor" },
    { id: "master", name: "Master" },
    { id: "phd", name: "PhD" },
    { id: "diploma", name: "Diploma" },
    { id: "none", name: "No Degree Required" },
  ];

  const publishDateOptions = [
    { id: 1, name: "Last 24 hours" },
    { id: 7, name: "Last 7 days" },
    { id: 15, name: "Last 15 days" },
    { id: 30, name: "Last 30 days" },
    { id: 60, name: "Last 60 days" },
  ];

  experianceOptions.forEach((option) => (option.type = "experience"));
  workplaceOptions.forEach((option) => (option.type = "workplace"));
  commitmentOptions.forEach((option) => (option.type = "commitment"));
  contractOptions.forEach((option) => (option.type = "contract"));
  degreeOptions.forEach((option) => (option.type = "degree"));
  publishDateOptions.forEach((option) => (option.type = "published"));

  return (
    <>
      <div className="d-flex flex-column gap-3">
        <CheckBox label="Visa Sponsorship" setSelected={setVisaSponsorship} />
        <CheckBox
          label="Relocation Support"
          setSelected={setRelocationSupport}
        />
        <CheckBox
          label="Remote From Anywhere"
          setSelected={setRemoteFromAnywhere}
        />
      </div>
      <MultiSelect
        options={experianceOptions}
        addFilter={addFilter}
        removeFilter={removeFilter}
        placeholder="Experience"
      />
      <MultiSelect
        options={workplaceOptions}
        addFilter={addFilter}
        removeFilter={removeFilter}
        placeholder="Workplace Type"
      />
      <MultiSelect
        options={commitmentOptions}
        addFilter={addFilter}
        removeFilter={removeFilter}
        placeholder="Commitment"
      />
      <MultiSelect
        options={contractOptions}
        addFilter={addFilter}
        removeFilter={removeFilter}
        placeholder="Contract"
      />
      <MultiSelect
        options={degreeOptions}
        addFilter={addFilter}
        removeFilter={removeFilter}
        placeholder="Degree"
      />
      <MultiSelect
        options={publishDateOptions}
        addFilter={addFilter}
        removeFilter={removeFilter}
        placeholder="Published Date"
      />
    </>
  );
};

export default Filters;
