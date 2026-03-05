import axios from "axios";
import { API_BASE_URL_DEVICE } from "../constants/config";

const api = axios.create({
  baseURL: API_BASE_URL_DEVICE,
  timeout: 30000,
  headers: {
    "Content-Type": "multipart/form-data",
  },
});

export const detectDisease = async (formData) => {
  try {
    console.log("Sending request to:", API_BASE_URL_DEVICE + "/detect");
    console.log("FormData:", formData);

    const response = await api.post("/detect", formData);
    console.log("Response:", response.data);
    return response.data;
  } catch (error) {
    console.error("API Error:", error);
    console.error("Error details:", error.message);
    console.error("Network error:", error.code);

    if (error.response) {
      console.error(
        "Response error:",
        error.response.status,
        error.response.data,
      );
      throw new Error(error.response.data.error || "Server error");
    } else if (error.request) {
      console.error("Request error - no response received");
      throw new Error("Network error. Please check your connection.", error);
    } else {
      console.error("Setup error:", error.message);
      throw new Error("Request failed. Please try again.", error);
    }
  }
};
