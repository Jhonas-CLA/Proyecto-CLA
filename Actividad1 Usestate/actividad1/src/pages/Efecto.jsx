import React, { useState, useEffect } from 'react';

function EjemploUseEffect() {
  const [contador, setContador] = useState(0);

  useEffect(() => {
    document.title = `Has clickeado ${contador} veces`;
  }, [contador]);  // Se ejecuta cada vez que el contador cambia

  return (
    <div>
      <p>Has clickeado {contador} veces</p>
      <button onClick={() => setContador(contador + 1)}>Clic aquí</button>
    </div>
  );
}

export default EjemploUseEffect;