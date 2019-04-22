import React, { Component } from "react";
import PropTypes from "prop-types";
class Profile extends Component {
    static propTypes = {
        endpoint: PropTypes.string.isRequired
    };
    state = {
        first_name: "",
        middle_name: "",
        last_name: "",
        email: ""
    };
    handleChange = e => {
        this.setState({ [e.target.name]: e.target.value });
    };
    handleSubmit = e => {
        e.preventDefault();
        const { first_name, middle_name, last_name, email } = this.state;
        const user = { first_name, middle_name, last_name, email };
        const conf = {
            method: "post",
            body: JSON.stringify(user),
            headers: new Headers({ "Content-Type": "application/json" })
        };
        fetch(this.props.endpoint, conf).then(response => console.log(response));
    };
    render() {
        const { first_name, middle_name, last_name, email } = this.state;
        return (
        <div className="column">
            <form onSubmit={this.handleSubmit}>
                <div className="field">
                    <label className="label">First Name</label>
                    <div className="control">
                        <input
                            className="input"
                            type="text"
                            name="first_name"
                            onChange={this.handleChange}
                            value={first_name}
                            required
                        />
                    </div>
                </div>
                <div className="field">
                    <label className="label">Middle Name</label>
                    <div className="control">
                        <input
                            className="input"
                            type="text"
                            name="middle_name"
                            onChange={this.handleChange}
                            value={middle_name}
                        />
                    </div>
                </div>
                <div className="field">
                    <label className="label">Last Name</label>
                    <div className="control">
                        <input
                            className="input"
                            type="text"
                            name="last_name"
                            onChange={this.handleChange}
                            value={last_name}
                            required
                        />
                    </div>
                </div>
                <div className="field">
                    <label className="label">Email</label>
                    <div className="control">
                        <input
                            className="input"
                            type="email"
                            name="email"
                            onChange={this.handleChange}
                            value={email}
                            required
                        />
                    </div>
                </div>
                <div className="control">
                    <button type="submit" className="button is-info">
                        Save Profile
                    </button>
                </div>
            </form>
        </div>
    );
  }
}
export default Profile;
