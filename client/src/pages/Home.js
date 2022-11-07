import React from "react";
import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";
import Chatbox from "../components/Chatbox";

const Home = () => {
  return (
    <div className="home">
      <Navbar />
      <div className="side-chat-area">
        <Sidebar />
        <div className="chat-area">
          <h2>Aashish Upadhyay</h2>
          <Chatbox />
        </div>
      </div>
    </div>
  );
};

export default Home;
