# satisfaccion_model

<p> Servidor con la capacidad de exponer un servicio web para predecir el nivel de satifacción en la vida de una pooblación de niños (entre 15 y 19 años) y abuelos. </p>

## Servicios web expuestos

<ul>
  <li>/prediccion -> Servicio POST
    <ul>
      <li>Parametros: 
          <ul>
           <li>file: Archivo a predecir</li>
            <li>isAbuelo: modelo de datos a predecir</li>
          </ul>
      </li>
      <p>Para obtener la plantilla del modelo se puede consultar en el siguiente enlace: https://prediction-satisfaction.herokuapp.com/ </p>
    </ul>
  </li>
  <li>/ -> Servicio GET </li>
  <p> Servicio get que obtiene el status page del servidor</p>
 </ul>
