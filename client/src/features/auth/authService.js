import axios from "axios";

LOGIN_URL = "http://127.0.0.1:8000/api/v1/auth/login/";
LOGOUT_URL = "http://127.0.0.1:8000/api/v1/auth/logout/";
REGISTER_URL = "http://127.0.0.1:8000/api/v1/auth/register/";

const register = async (userData) => {
  const config = {
    headers: {
      "Content-Type": "application/json",
    },
  };

  const response = await axios.post(REGISTER_URL, userData, config);
  return response.data;
};

const login = async (userData) => {
  const config = {
    headers: {
      "Content-Type": "application/json",
    },
  };

  const response = await axios.post(LOGIN_URL, userData, config);
  if (response.data) {
    localStorage.setItem("user", JSON.stringify(response.data));
  }
  return response.data;
};

const logout = async () => {
  const response = await axios.post(LOGOUT_URL);
  return localStorage.removeItem("user");
};

const authServices = { register, login, logout };

export default authServices;
