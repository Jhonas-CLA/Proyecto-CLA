import React, { useState, useEffect } from 'react';

function Componente4() {
  const [count, setCount] = useState(0);
  const [message, setMessage] = useState('');

  // Efecto 1: Imprimir el valor de "count" cuando cambia
  useEffect(() => {
    console.log('El valor de count ha cambiado:', count);
  }, [count]); // Se ejecuta cuando "count" cambia

  // Efecto 2: Establecer un mensaje después de 2 segundos
  useEffect(() => {
    const timer = setTimeout(() => {
      setMessage('¡Han pasado 2 segundos!');
    }, 2000);

    // Limpiar el timeout al desmontar el componente
    return () => clearTimeout(timer);
  }, []); // Este efecto solo se ejecuta una vez cuando el componente se monta

  return (
    <div>
      <h2>Contador: {count}</h2>
      <button onClick={() => setCount(count + 1)}>Aumentar contador</button>
      <p>{message}</p>
    </div>
  );
}

export default Componente4;