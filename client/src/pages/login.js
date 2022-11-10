import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";
import { login } from "../features/auth/authSlice";

const Login = () => {
  const user = useSelector((state) => state.auth.user);

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const dispatch = useDispatch();
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();

    const userData = {
      email: email,
      password: password,
    };

    console.log(userData);
    dispatch(login(userData));

    if (user) {
      navigate("/");
    }
  };

  return (
    <form className="login" onSubmit={handleSubmit}>
      <h1>Login</h1>
      <label for="email">Email</label>
      <input
        id="email"
        type="text"
        placeholder="someone@gmail.com"
        onChange={(e) => setEmail(e.target.value)}
        value={email}
      />

      <label for="password">Password</label>
      <input
        id="password"
        type="password"
        placeholder="your password"
        onChange={(e) => setPassword(e.target.value)}
        value={password}
      />

      <button className="btn btn-main" type="submit">
        Login
      </button>
    </form>
  );
};

export default Login;
