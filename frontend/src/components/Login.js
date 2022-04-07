// login page


import React from 'react';
import { withRouter } from "react-router-dom";


class Login extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            username: "",
        };
    }

    componentDidMount() {
        console.log('login component mounted');
    }
    componentWillUnmount() {
        console.log('login component unmounted');
    }

    updateUsername(event) {
        this.setState({
            username: event.target.value,
        });
    }

    render() {
        return (
            <div className="center h100">
                <div className="centerTitle">
                    <h1 className="loginTitle titleFont">Sign In</h1>
                </div>
                <div className="defaultFormClass" style={{ marginTop: '7px' }}>
                    Username: <input type="text" id="username" placeholder="username" onChange={this.updateUsername.bind(this)}></input><br />
                    Value: <b>{this.state.username}</b>
                </div>
            </div>
        );
    }
}

export default withRouter(Login);