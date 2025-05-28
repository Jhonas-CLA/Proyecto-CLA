import React, { useEffect } from 'react';

function Componente() {
  useEffect(() => {
    console.log("Este efecto se ejecuta solo una vez, al montarse el componente");

    // Aquí puedes poner código que solo se ejecute una vez, como una llamada a una API

  }, []);  // El array vacío significa que solo se ejecuta una vez

  return (
    <div>
      <p>Componente montado</p>
    </div>
  );
}

export default Componente;