import React from "react";
import ReactDOM from "react-dom";
import DataProvider from "./DataProvider";
import Table from "./Table";
import Profile from "./Profile";

const App = () => (
  <React.Fragment>
    <DataProvider endpoint="api/user/"
                  render={data => <Table data={data.results} />} />
    <Profile endpoint="api/user/" />
  </React.Fragment>
);

const wrapper = document.getElementById("app");

wrapper ? ReactDOM.render(<App />, wrapper) : null;
