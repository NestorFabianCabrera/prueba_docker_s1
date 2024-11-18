import React from 'react';
import Register from './Register';
import Login from './Login';
import './App.css';

function App() {
    return (
        <div>
            <h1>Registro</h1>
            <Register />
            <h1>Iniciar Sesión</h1>
            <Login />
        </div>
    );
}

export default App;
