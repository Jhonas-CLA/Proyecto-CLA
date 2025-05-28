import { useEffect, useState } from 'react';

function ComponenteConObjeto() {
  const [usuario, setUsuario] = useState({
    nombre: 'Urian Viera',
    edad: 35
  });

  // useEffect que depende del objeto "usuario"
  useEffect(() => {
    console.log(`Nombre del usuario: ${usuario.nombre}`);
    console.log(`Edad del usuario: ${usuario.edad}`);

    // Efecto de limpieza opcional
    return () => {
      console.log('Limpiando efecto del usuario...');
    };
  }, [usuario]); // Se ejecuta cada vez que cambia alguna propiedad del objeto "usuario"

  // Cambia los datos del usuario al hacer clic
  const actualizarUsuario = () => {
    setUsuario((prevUsuario) => ({
      ...prevUsuario,
      edad: prevUsuario.edad + 1,
    }));
  };

  return (
    <div>
      <p>Nombre: {usuario.nombre}</p>
      <p>Edad: {usuario.edad}</p>
      <button onClick={actualizarUsuario}>Aumentar Edad</button>
    </div>
  );
}

export default ComponenteConObjeto;