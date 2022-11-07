import React from "react";

const Login = () => {
  return (
    <div className="login">
      <h1>Login</h1>
      <label for="email">Email</label>
      <input id="email" type="text" placeholder="someone@gmail.com" />

      <label for="password">Password</label>
      <input id="password" type="password" placeholder="your password" />

      <button className="btn btn-main">Login</button>
    </div>
  );
};

export default Login;
