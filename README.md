# Talataa
prueba es propiedad privada de Talataa


El proyecto se realizo utilizando las siguientes librerias que s eencuentran en el:
=> requerimientos.txt

Fue creado utilizando el Lenguaje PYTHON 3 con el FrameWork DJANGO.
la base de datos esta en MySQL y la Base de datos es "talataadb", esta informacion esta inscrita en el archivo de "setting.py" del proyecto.

SE DEBE en cuenta que segun los requerimiento solicitados, los conductores no se crean como los pedidos por se tomo la libertidad de crear un listado en JSON de los posibles conductores en la ruta "apirest"->"fixtures"->"conductores_data.JSON" donde se pueden crear multiples conductores de un listado. Se tiene que tener en cuenta que una vez se tenga la lista de conductores se cargue con la siguiente instruccion en la terminal: " python manage.py loaddata conductores_data.json ". para que se alimente la tabla de Conductores antes de poder crear los pedidos.

SE DEBE tener en cuenta que este proyecto se diseño de dos maneras. Para ejecutarlo por peticiones o por un navegador simple. Puesto que hubo una confucion al momento de leer la prueba, donde no se aclara como sera el metodo de revision y estas dudas no se aclararon con las personas pertinentes.

=================================================

las rutas por peticiones son la siguentes:

>Consultar todos los pedidos metodo GET:
http://127.0.0.1:8000/apirest/pedidos/

>Agregar un pedido metodo POST(se debe de mandar un json con los campos y valores de los pedidos):
http://127.0.0.1:8000/apirest/pedidos/

EJ: {
      "nombre": "ejemplo",
      "apellido": "ejemplo",
      "correo": "ejemplo@gmail.com",
      "telefono": 333333333,
      "direccion": "ejemplo",
      "fecha_entrega": "9999-99-9",
      "franja_hora": 8
}

>Consultar un pedido en especifico, mandar el numero del id en la ruta metodo GET:
http://127.0.0.1:8000/apirest/pedidos/'<id>'

>Actualizar un pedido en especifico, mandar tanto el id como el json metodo PUT:
http://127.0.0.1:8000/apirest/pedidos/'<id>'

>eliminar un pedido en especifico, mandar tanto el id metodo PUT:
http://127.0.0.1:8000/apirest/pedidos/'<id>'

>Consultar todos los conductores metodo GET:
http://127.0.0.1:8000/apirest/conductores/

>Consultar todos los pedidos relacionados por conductor enviar el ID del conductor metodo GET:
http://127.0.0.1:8000/apirest/conductores/'<id>'
      
===================================================

Para verificar por proyecto utilizando las vistas se debe correr el Servidor de PYTHON-DJANGO con la instruccion: " python manage.py runserver ".
y las rutas las puede verificar en el archivo de las urls.py y sus respectivos endpoints.
ejemplo:
>Home: http://127.0.0.1:8000/

>Pedidos: http://127.0.0.1:8000/pedido/

>Conductores: http://127.0.0.1:8000/conductor/

Gracias por su atencion.

