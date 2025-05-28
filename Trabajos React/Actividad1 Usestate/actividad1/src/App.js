import logo from './logo.svg';
import './App.css';
import Interruptor from './pages/Interrptor.jsx';
import Lista from './pages/Lista.jsx';
import Componente from './pages/Vacia.jsx';
import Componente2 from './pages/Rest.jsx';
import Componente3 from './pages/Dependecias.jsx';
import Componente4 from './pages/Multiples.jsx';
import ComponenteConObjeto from './pages/Objeto.jsx';
import EjemploUseEffect from './pages/Efecto.jsx';
import ComponenteSinDependencias from './pages/Arraysin.jsx';
import ComponenteConDependenciaNula from './pages/Null.jsx';

import { BrowserRouter, Routes, Route } from 'react-router-dom';
import ToggleComponent from './pages/Toggle.jsx';
import React, { useState } from 'react';

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path='/' element={<Interruptor />} />
      </Routes> 
      <Routes>
        <Route path='/' element={<Lista />} />
      </Routes>
      <Routes>
        <Route path='/' element={<ToggleComponent />} />
      </Routes>
      <Routes>
        <Route path='/' element={<EjemploUseEffect />} />
      </Routes>
      <Routes>
        <Route path='/' element={<Componente />} />
      </Routes>
      <Routes>
        <Route path='/' element={<ComponenteSinDependencias />} />
      </Routes>
      <Routes>
        <Route path='/' element={<Componente2 />} />
      </Routes>
      <Routes>
        <Route path='/' element={<Componente3 />} />
      </Routes>
      <Routes>
        <Route path='/' element={<Componente4 />} />
      </Routes>
      <Routes>
        <Route path='/' element={<ComponenteConObjeto />} />
      </Routes>
      <Routes>
        <Route path='/' element={<ComponenteConDependenciaNula />} />
      </Routes>    
    </div>
  );
}

export default App;
