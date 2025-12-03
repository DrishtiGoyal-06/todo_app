import { Tag } from "@/types/types";
import axios from "axios";

export const getTagsAPI = async () => {
  const response = await axios.get<Tag[]>("https://todos-app-mkh4.onrender.com/api/v1/tags");


  return response.data;
};
