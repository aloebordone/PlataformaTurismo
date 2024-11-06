**TAREAS Y ESTADOS**
1. **Agregar información sobre las ciudades**: Moddificar el modelo de ciudades apra cargar información relevante para el turismo de la provincia. - Para agrgar la informacion de las ciudades van a tener que modificar la clase City en el archivo models.py y luego hacer la migracion para que impacten los cambios en la base de datos. Luego van a tener que modificar el template city_detail.html para mostrar la información nueva.
    *ESTADO*: Agregamos descripción al modelo. No hemos hecho migración ni cambios en tempkate city_detail.html, por lo que todavía no sabemos cómo impacta este cambio


2. **Árboles Binarios de Búsqueda**: Comentar todos los metodos del arbol binario de busqueda explicando apra que sirven y como funcionan.- Lean y comenten la clase ABB que esta en el archivo utils.py, estudien la implementacion completa que despues la van a tener que defender.
    *ESTADO*: Parcialmente realizado. Todavía nos faltan comentarios, porque estamos en proceso de entender cada una de sus partes

3. **Algoritmo de Dijkstra**: Implementar desde cero el algoritmo para encontrar la ruta más corta entre dos ciudades. La entrada serán las ciudades cargadas previamente, y la salida, la ruta óptima y la distancia. - Para calcular las rutas van a tener que implementar la función def dijkstra(start_city) y def get_shortest_path(start_city, end_city) en el archivo utils.py
    *ESTADO*: Aún no hemos implementado el algoritmo. Falta ver videos y entender cómo funciona.

+ modificar la carga de rutas para que al agregar una ruta ciudad1->ciudad2 50km también agregue la ruta ciudad2->ciudad1 50km
    *ESTADO*: Queremos averiguar cómo implementar este cambio, que nos parece mjuy útil. No lo hemos visto aún.

+ modificar el pryecto apra que puedan cargarse una foto de la ciudad y mostrarla en la página de la ciudad (ver manejo de archivos estaticos publicos en django)
    *ESTADO*: Aún no sabemos si vamos a implementar esto. 



**PLANIFICACION**
Jueves 7/11
Objetivo:
- Tener ideos de Django vistos y sacarnos dudas en clase

Viernes 8/11
Objetivo: 
 - Llegar a entender el algoritmo de dijkstra y tenerlo implementado
 - Tener el código comentado


Sábado 9/11 
Objetivo:
- Terminar código fuente.
- Testeo manual: diagramar casos de prueba y comenzar ejecución
- COmenzar con el guión de video

Domingo 10/11
Objetivo:
- Debuggear a partir de testeos
- analisis de complejidad
- Realización de informe
- Tener video grabado

Lunes 11/11
- Terminar testeos y desarrollo (en caso de no haber terminado)
- edición de video

