import React, { useState, useEffect } from 'react';

function Componente2() {
  const [datos, setDatos] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Definir una función asíncrona dentro de useEffect
    const fetchDatos = async () => {
      try {
        const response = await fetch('https://api.example.com/datos');
        const data = await response.json();
        setDatos(data);
      } catch (error) {
        console.error('Error al obtener los datos:', error);
      } finally {
        setLoading(false); // Marcar como cargado una vez se termine
      }
    };

    fetchDatos(); // Llamar a la función asíncrona

  }, []);  // El array vacío asegura que solo se ejecute una vez

  return (
    <div>
      <h2>Datos de la API</h2>
      {loading ? (
        <p>Cargando...</p>
      ) : (
        <pre>{JSON.stringify(datos, null, 2)}</pre>
      )}
    </div>
  );
}

export default Componente2;