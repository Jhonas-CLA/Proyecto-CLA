import React, { useState } from 'react';

function Seleccionador() {
  // Estado para almacenar el valor seleccionado
  const [seleccion, setSeleccion] = useState('');

  // Función que se ejecuta cuando el valor cambia
  const manejarCambio = (evento) => {
    setSeleccion(evento.target.value);
  };

  return (
    <div className='estilo'>
      <label htmlFor="opciones">Elige una opción:</label>
      <select id="opciones" value={seleccion} onChange={manejarCambio}>
        <option value="">--Seleccione--</option>
        <option value="opcion1">Opción 1</option>
        <option value="opcion2">Opción 2</option>
        <option value="opcion3">Opción 3</option>
      </select>
      <p>Has seleccionado: {seleccion}</p>
    </div>
  );
}

export default Seleccionador;