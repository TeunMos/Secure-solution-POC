import React from "react";
import { useEffect } from "react";
import "./App.css";
import { io } from "socket.io-client";
import { useState } from "react";

function App() {
  const [luggageList, setLuggageList] = useState([]);

  const [gateList, setGateList] = useState([]);

  useEffect(() => {
    const socket = io("http://localhost:3000");

    socket.on("connect", () => {
      console.log("connected");
      socket.emit("getLuggage");
    });

    socket.on("disconnect", () => {
      console.log("disconnected");
    });

    socket.on("allLuggage", (data) => {
      setLuggageList(data);
    });

    socket.on('allGates', (data) => {
      setGateList(data);
    });

    socket.on("luggageAdded", (data) => {
      setLuggageList([...luggageList, data]);
    });

    socket.on("luggageUpdated", (data) => {
      setLuggageList(
        luggageList.map((luggage) => {
          if (luggage.id === data.id) {
            return data;
          }
          return luggage;
        })
      );
    });

    socket.on("luggageDeleted", (data) => {
      setLuggageList(luggageList.filter((luggage) => luggage.id !== data.id));
    });
  }, []);

  useEffect(() => {
    console.log(luggageList);
  }, [luggageList]);

  return (
    <div className="App">
      <h1>Bagage Tracking</h1>
      <table id="luggageTable">
        <thead>
          <tr>
            <th>tag</th>
            <th>location</th>
          </tr>
        </thead>
        <tbody>
          {luggageList.map((luggage) => (
            <tr key={luggage.id}>
              <td>{luggage.id}</td>
              <td>{luggage.location}</td>
            </tr>
          ))}
        </tbody>
      </table>
      

    </div>
  );
}

export default App;
