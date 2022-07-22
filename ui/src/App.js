import Login from './Login';
import MainScreen from './MainScreen';
import React, { useState } from 'react';


function App() {
  const [jwt, setJwt] = useState("");
  return (
    <div style={{
      width:480,
      height:600,
      margin:32,
      // backgroundColor:'blue'
      border:'1px solid black'
    }}>
      {!jwt && <Login onLogin={jwt => setJwt(jwt)} />}
      {!!jwt && <MainScreen jwt={jwt} onLogout={() => setJwt("")} />}

    </div>
  );
}

export default App;
