import React, { Component } from 'react';

import GoogleLogin from 'react-google-login';
import googleLogin from "./services/googleLogin"

import './App.css';

export class Login extends Component {

  render() {


    const responseGoogle = async(response) => {
      let googleResponse  = await googleLogin(response.accessToken)
      console.log(googleResponse);
      console.log(response.profileObj);
      sessionStorage.setItem("userData", JSON.stringify(response));
    }

    return (
      <div className="App">
        <h1>LOGIN WITH GOOGLE</h1>

       
        <br />
        <br />

        <GoogleLogin
          clientId="926339133599-ed7g1bt0mk4qu0qc1vpoo9mnkneuefn8.apps.googleusercontent.com"
          buttonText="LOGIN WITH GOOGLE"
          onSuccess={responseGoogle}
          onFailure={responseGoogle}

        />

      </div>
    );
  }
}

export default Login;
