import React, { useState, useEffect } from 'react';

function Componente3() {
  const [query, setQuery] = useState('react');
  const [datos, setDatos] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchDatos = async () => {
      setLoading(true);
      try {
        const response = await fetch(`https://api.example.com/search?q=${query}`);
        const data = await response.json();
        setDatos(data);
      } catch (error) {
        console.error('Error al obtener los datos:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchDatos(); // Llamar a la función asíncrona

  }, [query]); // El efecto se ejecuta cada vez que cambia 'query'

  return (
    <div>
      <h2>Buscar Datos</h2>
      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)} // Actualizar la query
        placeholder="Buscar..."
      />
      {loading ? (
        <p>Cargando...</p>
      ) : (
        <pre>{JSON.stringify(datos, null, 2)}</pre>
      )}
    </div>
  );
}

export default Componente3;