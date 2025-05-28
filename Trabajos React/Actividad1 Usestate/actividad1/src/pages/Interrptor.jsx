import React, { useState } from 'react';

function Interruptor() {
  // Estado inicial: apagado (false)
  const [encendido, setEncendido] = useState(false);

  // Función para cambiar el estado
  const manejarClick = () => {
    setEncendido(!encendido);
  };

  return (
    <div className='estilo'>
      <p>El interruptor está {encendido ? 'Encendido' : 'Apagado'}</p>
      <button className='boton' onClick={manejarClick}>
        {encendido ? 'Apagar' : 'Encender'}
      </button>
    </div>
  );
}

export default Interruptor;