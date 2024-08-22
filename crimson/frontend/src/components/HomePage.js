import React, { Component } from "react";
import RoomJoinPage from "./RoomJoinPage";
import CreateRoomPage from "./CreateRoomPage";
import { BrowserRouter as Router, Routes, Route, Link, Redirect } from "react-router-dom";


export default class HomePage extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <Router>
        <Routes> {/* Substitua Switch por Routes */}
          <Route exact path="/">
            <p>This is the home page</p>
          </Route>
          <Route path="/join" element={<RoomJoinPage />} /> {/* Use 'element' em vez de 'component' */}
          <Route path="/create" element={<CreateRoomPage />} /> {/* Use 'element' em vez de 'component' */}
        </Routes>
      </Router>
    );
  }
}