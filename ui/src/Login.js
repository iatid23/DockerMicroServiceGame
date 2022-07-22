import React, { useState } from 'react';

function Login(props) {
    const [email, setEmail] = useState("");
    const [err, setErr] = useState("");
    return (
      <div style={{
        margin:16
    }}>
        <p > Auth screen </p>
        <br/>
        <input type="text" value={email} onChange={event => {
            setEmail(event.target.value)
        }} />
        <br/>
        <br/>
        <button style={{
            
        }} onClick={() => {
            fetch('http://127.0.0.1:8000/login/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({email})
            }).then(res=>res.json())
            .then(res => {
                setErr(res.err)
                res.jwt && props.onLogin(res.jwt)
                // console.log(res)
            });
        }}> Login</button>
        <button style={{
            margin:32
        }} onClick={() => {
            fetch('http://127.0.0.1:8000/signup/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({email})
            }).then(res=>res.json())
            .then(res => {
                setErr(res.err)
                res.jwt && props.onLogin(res.jwt)
                // console.log(res)
            });
        }}> Singup</button>
        <br />
        <br />
        <p style={{color:"red"}}> {err} </p>
      </div>
    );
  }
  
  export default Login;
  