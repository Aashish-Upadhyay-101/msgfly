import React from "react";
import { useSelector } from "react-redux";

const Navbar = () => {
  const user = useSelector((state) => state.auth.user);

  return (
    <div className="navbar">
      <h2>Msgfly</h2>
      <p>Hello, {user.user.username}</p>
    </div>
  );
};

export default Navbar;
