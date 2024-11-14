Entrega 3. Bordone Aloe - Ramirez Verónica 

Código fuente y documentación del proyecto:
    Codigo fuente: 
    Comentarios en el código: se comenta el código de los archivos models.py y util.py
    Decisiones de diseño: se elige trabajar con ciudades de la provincia de Santa Cruz 

Detalle: 
Creen un tag en github con lo que van a entregar.



Creen un archivo Readme.md en el repo Con
    Explicación del proyecto:
    Este proyecto se realiza en vistas de cumplimentar con los requerimientos académicos de la finalización del segundo año de la carrera terciaria Tecnicatura Superior en Desarrollo de Software dictada por el Instituto Técnico Superior Córdoba Sede Villa Libertador. 
    El mismo refiere a la creación de una aplicación web con una funcionalidad similar a la del conocido GPS y le permite al usuario elegir distintas ciudades como punto de partida y llegada, proporcionandole el beneficio de ofrecerle la ruta mas corta para llegar a destino. Muestra las ciudades por las que va a pasar para llegar a destino y acompañando el nombre de cada ciudad, la página muestra una descripción de la misma y su población. 



    Explicación de que se implementó en el proyecto. 

    En la estructura del código se trabajo en los archivos:

    city-details.html: donde se agregaron los campos que mostrarán en la página al usuario nombre, descripción y población, y cuya información será cargada por un administrador. Estos campos fueron crados como clases en el html lo que permitirá darle un estilo si se agrega un archivo css.

    models.py: aca se definio las clases City y Routes, en esta última su relación con la primera mencionada agregando una estructura en cascada atento a cualquiera modificación de rutas o ciudades. En la clase ruta se condicionó a la creación de cada objeto para que sea único en su creación siendo necesario importar el módulo UniqueConstraint. Por último se creo una función create_inverse_route que se ejecuta cada vez que recepta la creación de un evento del modelo Route para crear la ruta inversa a la reciente creada. Para su funcionalidad fue necesario importar los módulos post_save y receiver.

    utils.py: en este archivo se desarrollo el código del algoritmo dijkstra que toma como punto de partida una ciudad, y guarda en un diccionario las distancias hacia todas las ciudades qut tiene como vecinas. Gracias al módulo priority_queue crea una cola de prioridad donde acomoda las distancias encontradas de menor a mayor. Extrae el último elemento de la cola y asigan sus elementos a dos variables que luego usa para ir guardando el recorrido entre ciudades y la distancia total

    tests.py: en este archivo se implementaron pruebas de uso para verificar que todo esté funcionando correctamente. Para ello nos encontramos con dificultades como la configuración de Django y su entorno, ya que no podríamos ejecutar el archivo en consola. Tuvimos que importar os y establecer la configuración del entorno dentro del mismo archivo (ayuda de chat gpt) y los test dieron todos OK.

    city_detail.html: se modificaron algunas líneas para que se lea mejor la descripción y habilitar las imágenes.

    urls.py: se modificaron y agregaron líneas de código para habilitar la carga de imágenes

    tests.py: se crearon pruebas para comprobar el buen funcionamiento. 

    - el analisis de complejidad algortmica de dijkstra: 
    En la inicialización, crea el diccionario, distances y previous_cities: O(1). Insertar el nodo en la cola de prioridad: O(log v). Bucle principal: extraer el nodo con la menor distancia de la cola de prioridad O(log v), para cada nodo recorrer sus vecinos (E veces en total): O(E). Actualizar la distancia y volver a insertar en la cola de prioridad: O(log v)
        Notación Big-O
        O ((V + E)*log V)
        referencias:
        (V) es el número de vertices (ciudades)
        (E) es el número de aristas (rutas)


    En funcionamento: carga de rutas y ciudades, carga de descripción y población, calculo de distancia mas corta y devoluión del recorrido que realziar por las ciudades para llegar a destino. Imágenes ilustrativas de cada ciudad, visualizacióon de datos importantes como descripción y población. 


    Mejoras: Se puede hacer más vistoso para el usuario, con otros colores y tipografías. 


    