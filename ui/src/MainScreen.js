import React, { useState, useEffect } from 'react';
import jwt_decode from "jwt-decode";
import GameScreen from "./GameScreen"

function MainScreen(props) {
    const decoded = jwt_decode(props.jwt);
    const email = decoded.email
    const [showGame, setShowGame] = useState(false);
    const [isHavePrevGame, setIsHavePrevGame] = useState(false);
    useEffect(() => {
        fetch('http://127.0.0.1:8001/is_have_active_game/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({jwt: props.jwt})
        }).then(res=>res.json())
        .then(res => {
            setIsHavePrevGame(res.having_game)
        });
    },[showGame])
    if(showGame) {
        return <GameScreen jwt={props.jwt} onBackToMainScreen={() => {
          setShowGame(false)  
        }}/>
    }
    return (
      <div style={{
        margin:16
    }}>
        <h3> Main screen </h3>
        <p> login as {email}</p>
        <br/>
        <br/>
        <button style={{
            // margin:32
        }} onClick={() => {
            fetch('http://127.0.0.1:8001/start_new_game/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({jwt: props.jwt})
            }).then(res=>res.json())
            .then(res => {
                setShowGame(true)
            });
        }}> Start New Game</button>
        <br/>
        <br/>
        {isHavePrevGame && <button onClick={() => {
            setShowGame(true)
        }}> Back To Active Game </button>}
        <br/>
        <br/>
        <button style={{
            // margin:32
        }} onClick={() => {
            props.onLogout()
        }}> LogOut</button>
      </div>
    );
  }
  
  export default MainScreen;
  