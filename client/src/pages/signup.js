import React from "react";

const Signup = () => {
  return (
    <div className="login">
      <h1 style={{ marginTop: "-6rem" }}>Signup</h1>
      <label for="firstname">First name</label>
      <input id="firstname" type="text" placeholder="first name" />

      <label for="lastname">Last name</label>
      <input id="lastname" type="text" placeholder="last name" />

      <label for="username">Username</label>
      <input id="username" type="text" placeholder="username" />

      <label for="email">Email</label>
      <input id="email" type="text" placeholder="someone@gmail.com" />

      <label for="password">Password</label>
      <input id="password" type="password" placeholder="your password" />

      <label for="re_password">Confirm Password</label>
      <input
        id="re_password"
        type="password"
        placeholder="your password (again)"
      />

      <button style={{ marginBottom: "rem" }} className="btn btn-main">
        Signup
      </button>
    </div>
  );
};

export default Signup;
