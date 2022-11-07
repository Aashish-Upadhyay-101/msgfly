import React from "react";

const Chatbox = () => {
  return (
    <div className="chatbox">
      <div className="message-area">
        <div>
          <div className="sender">
            <h4>Aashish Upadhyay</h4>
            <p>Your message dummy but i dont think.</p>
          </div>
          <div className="sender">
            <h4>Aashish Upadhyay</h4>
            <p>Your message dummy but i dont think.</p>
          </div>
          <div className="sender">
            <h4>Aashish Upadhyay</h4>
            <p>Your message dummy but i dont think.</p>
          </div>
          <div className="receiver">
            <h4>Aashish Upadhyay</h4>
            <p>Your message dummy but i dont think.</p>
          </div>
          <div className="sender">
            <h4>Aashish Upadhyay</h4>
            <p>Your message dummy but i dont think.</p>
          </div>
          <div className="receiver">
            <h4>Aashish Upadhyay</h4>
            <p>Your message dummy but i dont think.</p>
          </div>
          <div className="receiver">
            <h4>Aashish Upadhyay</h4>
            <p>Your message dummy but i dont think.</p>
          </div>
          <div className="sender">
            <h4>Aashish Upadhyay</h4>
            <p>Your message dummy but i dont think.</p>
          </div>
        </div>
      </div>
      <form className="send-message">
        <input type="text" placeholder="write your message..." />
        <button className="send-btn">send</button>
      </form>
    </div>
  );
};

export default Chatbox;
