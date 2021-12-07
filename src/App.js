
import './App.css';
import React from "react";
import { BrowserRouter, Switch, Route } from "react-router-dom";

import Navbar from "./components/Navbar";
import CsvReader from './components/CsvReader'

import Home from "./pages/Home";
import CreateAccount from "./pages/CreateAccount";
import Login from "./pages/Login";
import Profile from "./pages/Profile";
import Results from "./pages/Results";



function App() {
  var reactDOM;
  /*function dom(DOM){
    reactDOM = DOM;
    CsvReader().csvDom(reactDOM);
  }*/
  return (
    <BrowserRouter>
      <Navbar />
      <div className="container mt-2" style={{ marginTop: 40 }}>
        <Switch>

          <Route exact path="/">
            <Home />
          </Route>
          <Route path="/createAccount">
            <CreateAccount />
          </Route>
          <Route path="/profile">
            <Profile />
          </Route>
          <Route path="/login">
            <Login />
          </Route>
          <Route path="/results">
            <Results />
            <CsvReader />
          </Route>
          
        </Switch>
      </div>
    </BrowserRouter>
  );
}

export default App;