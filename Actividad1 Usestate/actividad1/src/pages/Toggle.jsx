import React, { useState } from 'react';

function ToggleComponent() {
  const [isVisible, setIsVisible] = useState(false);

  return (
    <div className='estilo'>
      <button className='boton' onClick={() => setIsVisible(!isVisible)}>
        {isVisible ? 'Ocultar' : 'Mostrar'}
      </button>
      
      {isVisible && (
        <div>
          ¡Este contenido se puede mostrar u ocultar!
        </div>
      )}
    </div>
  );
}

export default ToggleComponent;
