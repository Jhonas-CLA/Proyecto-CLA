import { useEffect, useState } from 'react';

function ComponenteConDependenciaNula() {
  const [data, setData] = useState(null);

  // Este useEffect depende de "data", y se ejecutará cada vez que "data" cambie
  useEffect(() => {
    if (data === null) {
      console.log('Data está en null');
    } else if (data === undefined) {
      console.log('Data está en undefined');
    } else {
      console.log(`Data tiene valor: ${data}`);
    }
  }, [data]); // El efecto se ejecuta cada vez que "data" cambia, incluso si cambia a null o undefined

  // Simula cambios de estado
  const establecerData = (valor) => setData(valor);

  return (
    <div>
      <p>{data !== null && data !== undefined ? `Data: ${data}` : 'Data es null o undefined'}</p>
      <button onClick={() => establecerData('Nuevo valor')}>Establecer Data</button>
      <button onClick={() => establecerData(null)}>Establecer null</button>
      <button onClick={() => establecerData(undefined)}>Establecer undefined</button>
    </div>
  );
}

export default ComponenteConDependenciaNula;