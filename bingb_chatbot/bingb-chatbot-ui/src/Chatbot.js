import React, { useState } from "react";
import axios from "axios";

const Chatbot = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  const sendMessage = async () => {
    if (!input.trim()) return;
  
    const userMessage = { text: input, sender: "user" };
    setMessages([...messages, userMessage]);
  
    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/webhook/",
        {
          queryResult: {
            intent: { displayName: "UserQuery" },
            queryText: input,
          },
        },
        {
          headers: { "Content-Type": "application/json" },
        }
      );
  
      const botMessage = { text: response.data.fulfillmentText, sender: "bot" };
      setMessages((prevMessages) => [...prevMessages, botMessage]);
    } catch (error) {
      console.error("Error fetching chatbot response:", error);
    }
  
    setInput("");
  };
  
  return (
    <div style={{ 
        display: "flex", 
        justifyContent: "center", 
        alignItems: "center", 
        height: "100vh",  // Full viewport height
        backgroundColor: "#F5F5F5" // Optional: Light gray background
      }}>
        <div style={{ 
          maxWidth: "400px", 
          width: "100%", 
          margin: "auto", 
          padding: "20px", 
          border: "1px solid #ccc", 
          backgroundColor: "#fff", // White chat background
          borderRadius: "10px", // Rounded corners
          boxShadow: "0px 4px 10px rgba(0, 0, 0, 0.1)" // Light shadow
        }}>
          <h2 style={{ textAlign: "center", color: "#00592D" }}>BingB Chatbot</h2> {/* University Color */}
          <div style={{ 
            height: "300px", 
            overflowY: "auto", 
            border: "1px solid gray", 
            padding: "10px", 
            borderRadius: "5px"
          }}>
            {messages.map((msg, index) => (
              <div key={index} style={{ 
                textAlign: msg.sender === "user" ? "right" : "left",
                marginBottom: "10px"
              }}>
                <strong style={{ color: msg.sender === "user" ? "#00592D" : "#000" }}>
                  {msg.sender === "user" ? "" : "BingB: "} 
                </strong> 
                {msg.text}
              </div>
            ))}
          </div>
          <div style={{ marginTop: "10px", display: "flex" }}>
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="Ask something..."
              style={{ flex: "1", padding: "8px", borderRadius: "5px", border: "1px solid #ccc" }}
            />
            <button 
              onClick={sendMessage} 
              style={{ 
                padding: "8px", 
                marginLeft: "5px", 
                borderRadius: "5px", 
                backgroundColor: "#00592D", // Binghamton Green
                color: "#fff", 
                border: "none",
                cursor: "pointer"
              }}>
              Send
            </button>
          </div>
        </div>
      </div>
        );
};

export default Chatbot;
