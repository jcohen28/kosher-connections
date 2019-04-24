import React, { Component } from 'react';
import './App.css';

import DataProvider from "./components/DataProvider";
import NavHeader from "./components/NavHeader";
import Profile from "./components/Profile";
import Table from "./components/Table";

class App extends Component {
  render() {
    return (
      <div className="App">
        { NavHeader }
        <DataProvider endpoint="api/user/"
                  render={data => <Table data={data.results} />} />
        <Profile endpoint="api/user/" />
      </div>
    );
  }
}

export default App;
