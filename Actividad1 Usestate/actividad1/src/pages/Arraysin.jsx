import { useEffect, useState } from 'react';

function ComponenteSinDependencias() {
  const [contador, setContador] = useState(0);

  // Este useEffect se ejecuta después de cada renderizado
  useEffect(() => {
    console.log('El componente ha sido renderizado o actualizado');

    // Función de limpieza (opcional) que se ejecutará antes de que el efecto se ejecute nuevamente o cuando el componente se desmonte
    return () => {
      console.log('Limpiando efecto');
    };
  }); // Sin array de dependencias: se ejecuta en cada renderizado

  const incrementarContador = () => {
    setContador(contador + 1);
  };

  return (
    <div>
      <p>Contador: {contador}</p>
      <button onClick={incrementarContador}>Incrementar</button>
    </div>
  );
}

export default ComponenteSinDependencias;