# eb2
## Importante
La mayor parte del desarrollo realizado se encuentra en el modulo /easy_broker/properties/, lo demas en gran parte es generado por el framework.
## Instrucciones de instalacion
Para poder ejecutar este proyecto es necesario tener instalado conda. Para lo cual yo recomiendo instalar miniconda para una instalación ligera.
* https://docs.conda.io/en/latest/miniconda.html

1
Una vez instalado, es necesario abrir una consola y crear un entorno virtual nuevo con el siguiente comando.
```
conda create -n easy_broker python==3.10
conda activate easy_broker
```

2
Dirigirnos a la ubicación del archivo requirements.txt desde la consola y ejecutar el siguiente comando.
```
pip install -r requirements.txt
```

3
Finalmente, dirigirnos a la ubicación del archivo manage.py y ejecutar el siguiente comando.
```
python manage.py runserver
```

4
¡Listo! Ahora puedes navegar en el sistema utilizando la dirección señalada en la consola.
```
http://127.0.0.1:8000/
```

## Capturas
Listado
![Lista](/img/Screenshot_1.png?raw=true "Vistazo general 1")
![Vistazo general 2](/img/Screenshot_2.png?raw=true "Vistazo general 1")
![Vistazo general 3](/img/Screenshot_3.png?raw=true "Vistazo general 1")
![Vistazo general 4](/img/Screenshot_4.png?raw=true "Vistazo general 1")
Detalles
![Detalles](/img/Screenshot_5.png?raw=true "Detalles")
Slider
![Slider](/img/Screenshot_6.png?raw=true "Slider")
Uso de formulario
![Uso de formulario](/img/Screenshot_7.png?raw=true "Uso de formulario")
Notificacion
![Notificacion](/img/Screenshot_8.png?raw=true "Notificacion")
Paginacion
![Paginacion](/img/Screenshot_9.png?raw=true "Paginacion")
Si el usuario modifica la url, y esta no existe tenemos un 404
![404](/img/Screenshot_10.png?raw=true "404")
![404](/img/Screenshot_11.png?raw=true "404")

## Notas
A continuación escribo una retrospectiva del desarrollo de este proyecto.
Dado el tiempo que se tenía para resolver la prueba técnica, se tomaron ciertas decisiones para poder terminarlo en el tiempo, y si bien no se sacrifica en gran manera la calidad, la estructura se puede perder un poco.

Un claro ejemplo es el archivo llamado easy_broker.py, la cual contiene la clase del cliente para poder consumir la API de easy broker. Esta clase debería tener una mejor localización en el directorio, quizá en alguna carpeta de utilería, y separarla en cierta manera del módulo de Django llamado properties.

En mi caso una parte que me costó fue realizar el frontend de la plataforma, si bien, este no sería calificado en gran manera, sí que quería obtener un mejor resultado, una parte relacionada a backend, frontend que me hizo falta fue poner una imagen default para las propiedades que no tuvieran imagenes.

De igual manera, existen partes de mi código donde se puede agregar más documentación en forma de comentario sobre las funciones, en este caso, los controladores.

Finalmente, el poder juntar todas las funcionalidades del sistema, así como validaciones son lo que representaron un mayor reto, siempre se buscó tener consistencia, utilizar el código más limpio posible y sin que se perdiera la estructura que sugiere el framework.
