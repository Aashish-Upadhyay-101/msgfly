import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";
import { register } from "../features/auth/authSlice";

const Signup = () => {
  const user = useSelector((state) => state.auth.user);

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [firstname, setFirstname] = useState("");
  const [lastname, setLastname] = useState("");
  const [username, setUsername] = useState("");
  const [password2, setPassword2] = useState("");

  const dispatch = useDispatch();
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();

    const userData = {
      username,
      firstname,
      lastname,
      email,
      password,
      password2,
    };

    console.log(userData);
    dispatch(register(userData));

    if (user) {
      navigate("/");
    }
  };

  return (
    <form className="login" onSubmit={handleSubmit}>
      <h1 style={{ marginTop: "-6rem" }}>Signup</h1>
      <label for="firstname">First name</label>
      <input
        id="firstname"
        type="text"
        placeholder="first name"
        value={firstname}
        onChange={(e) => setFirstname(e.target.value)}
      />

      <label for="lastname">Last name</label>
      <input
        id="lastname"
        type="text"
        placeholder="last name"
        value={lastname}
        onChange={(e) => setLastname(e.target.value)}
      />

      <label for="username">Username</label>
      <input
        id="username"
        type="text"
        placeholder="username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />

      <label for="email">Email</label>
      <input
        id="email"
        type="text"
        placeholder="someone@gmail.com"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />

      <label for="password">Password</label>
      <input
        id="password"
        type="password"
        placeholder="your password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />

      <label for="re_password">Confirm Password</label>
      <input
        id="re_password"
        type="password"
        placeholder="your password (again)"
        value={password2}
        onChange={(e) => setPassword2(e.target.value)}
      />

      <button
        style={{ marginBottom: "rem" }}
        className="btn btn-main"
        type="submit"
      >
        Signup
      </button>
    </form>
  );
};

export default Signup;
