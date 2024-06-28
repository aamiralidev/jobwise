import { apiClient } from "./ApiClient";

export const getJobs = (pageNo = 1, filters = []) => {
  return apiClient.get(`jobs/?page=${pageNo}`);
};
