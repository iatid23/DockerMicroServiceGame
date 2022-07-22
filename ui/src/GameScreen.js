import React, { useState, useEffect } from 'react';

function GameCell(props) {
    return <div style={{
        width:120,
        height:120,
        border:'solid 1px black',
        fontSize:70,
        display:'flex',
        alignItems:'center',
        justifyContent:'center',
        cursor:'pointer'
    }} onClick={props.onCellClick}>
        {props.data}
    </div>
}

function GameRow(props) {
    return <div style={{
        display:'flex'
    }}>
        {props.data.map((_,i) => <GameCell onCellClick={() => {
            props.onCellClick(i)
        }} data={_} key={i}/>)}
    </div>
}

function GameScreen(props) {
    const [updateGameState, setUpdateGameState] = useState(0);
    const [gameState, setGameState] = useState({});
    useEffect(() => {
        fetch('http://127.0.0.1:8001/get_game_state/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({jwt: props.jwt})
        }).then(res=>res.json())
        .then(res => {
            // setErr(res.err)
            // res.jwt && props.onLogin(res.jwt)
            if(res.turn !== res.player_play && !res.is_over) {
                setTimeout(() => setUpdateGameState(updateGameState + 1),500)
            }
            setGameState(res)
        });
    },[updateGameState])
    return (
      <div style={{
        margin:16
    }}>
        <h3> Game screen </h3>
            {/* <p> turn:   </p> */}
            {gameState.board && gameState.board.map((_,i) => <GameRow onCellClick={j => {
                fetch('http://127.0.0.1:8001/player_move/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        row:i, 
                        col:j,
                        jwt: props.jwt
                    })
                }).then(res=>res.json())
                .then(res => {
                    setUpdateGameState(updateGameState + 1)
                });
            }} key={i} data={_}/>) }
            {!gameState.is_over && <p> waiting for {gameState.turn === gameState.player_play ? "PLAYER":"CPU"} ({gameState.turn}) move</p>}
            {!!gameState.winner && <h4> {gameState.winner} win! </h4>}
            {!gameState.winner && gameState.is_over && <h4> tie! </h4>}
        <button onClick={props.onBackToMainScreen}> Back </button>
      </div>
    );
  }
  
  export default GameScreen;
  