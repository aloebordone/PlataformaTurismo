import heapq # Importa heapq para gestionar la cola de prioridad, cada nodo siempre será menor o igual que sus hijos y será la base de la raíz del arbol
from .models import City, Route #importa la clase ciudad y ruta del archivo model

def dijkstra(start_city): #se le pasa una ciudad por parametro desde donde se quiere empezar
    distances = {start_city: 0} #diccionario que guarda nombre de las ciudades(clave) y las distancias mas cortas(valor) encontradas la ciudad parámetro.
    previous_cities = {start_city: None} #permite construir el camino mas corto guardando el nodo anterior(ciudad) distancia mas corta por el que paso.
    priority_queue = [(0, start_city)] # crea cola de prioridad para recorrer los nodos del grafo en orden de la distancia mas corta
 
 
    while priority_queue: # mientras haya elementos en la cola para recorrer en el grafo
         
        current_distance, current_city = heapq.heappop(priority_queue) #elimina el elemento con la menor distancia y la ciudad y asigna los valores en las dos variables current

        #compara si la distancia actual extraida de la cola es mayor a la obtenida del diccionario
        if current_distance > distances.get(current_city, float('inf')): #en el diccionario distances busca la distancia asociada a la ciudad current_city
            continue

        
        for route in list(current_city.route_start.all()) + list(current_city.route_end.all()):#Recorre las rutas que salen desde la ciudad actual y las que llegan a la ciudad actual (para un grafo no dirigido)
           
            neighbor = route.end_city if route.start_city == current_city else route.start_city  #Verifica si la ciudad de inicio es la ciudad actual, entonces el vecino será la ciudad destino. Sino la ciudad vecino será la actual
            distance = current_distance + route.distance #suma las distancias

       
            if distance < distances.get(neighbor, float('inf')): #verifica si la nueva distancia es menor a la ya registrada para ese vecino
                distances[neighbor] = distance #si es menor, la asigna como la nueva distancia 
                previous_cities[neighbor] = current_city #actualiza la ciudad del vecino a la actual
                heapq.heappush(priority_queue, (distance, neighbor)) #agrega la distancia y el vecino a la cola de prioridad

    return distances, previous_cities


def get_shortest_path(start_city, end_city): #define una función para obtener el camino más corto dado una ciudad de inicio y una de llegada
    distances, previous_cities = dijkstra(start_city) #se calculan distancias mínimas y ciudades previas con el algoritmo de dijkstra desde la ciudad de inicio
    path = [] #se arma una lista con las ciudades que conforman la ruta
    city = end_city #ciudad de llegada

    while previous_cities[city]: #recorre el diccionario de ciudades previas para construir el recorrido
        path.insert(0, city)
        city = previous_cities[city]
    path.insert(0, city)

    return path, distances[end_city] #retorna el camino y la distancia final

class ArbolBinarioBusqueda: #se crea una clase para crear un Árbol Binario de Búsqueda

    def __init__(self): #inicia un ábol vacío
        self.raiz = None #define la raíz como none inicialmente
        self.tamano = 0 #inicia un contador para saber el tamaño

    def agregar(self,clave,valor): #método para agregar un nodo
        if self.raiz: #se fija si ya existe una raíz en el árbol, y si la hay...
            self._agregar(clave,valor,self.raiz) #llama a la función _agregar
        else: #si no había raíz
            self.raiz = NodoArbol(clave,valor) #crea una raíz con el nodo dado utilizando la clase NodoArbol
        self.tamano = self.tamano + 1 #al agregar un nodo, aumenta 1 al contador de tamaño

    def _agregar(self,clave,valor,nodoActual): #es una función recursiva para agregar un nodo en el lugar correcto
        if clave < nodoActual.clave:#si la clave del nodo dado es menor a la del nodo actual...
            if nodoActual.tieneHijoIzquierdo(): #si el nodo actual tiene hijo izquierdo
                self._agregar(clave,valor,nodoActual.hijoIzquierdo) #recurre a la izquierda
            else: #si no tiene hijo izquierdo
                nodoActual.hijoIzquierdo = NodoArbol(clave,valor,padre=nodoActual) #agrega hijo izquierdo
        else: #si no ingresó al primer if (clave menor a clave del nodo actual)
            if nodoActual.tieneHijoDerecho(): #si tiene hijo derecho
                self._agregar(clave,valor,nodoActual.hijoDerecho) #recurre a la derecha
            else: #si no
                nodoActual.hijoDerecho = NodoArbol(clave,valor,padre=nodoActual) #agrega hijo derecho

    def __setitem__(self,c,v):
        self.agregar(c,v)

    def obtener(self,clave): #obtiene el valor de una claver del árbol
        if self.raiz: #si el árbol tiene una raíz...
            res = self._obtener(clave,self.raiz) #llama a _obtener
            if res: #si encuentra el nodo
                return res.cargaUtil #devuelve el valor del nodo
            else: #si no
                return None #devuelve None
        else: #si el árbol no tiene raíz
            return None #devuelve NOne

    def _obtener(self,clave,nodoActual): #recursividad para buscar un nodo con una clave dada
        if not nodoActual: #si el nodo actual es None, no encontró la clave y devuelve None
            return None
        elif nodoActual.clave == clave: #compara la clave dada con la del nodo actual, si es igual, devuelve el nodo actual
            return nodoActual
        elif clave < nodoActual.clave: #compara la clave dada con la del nodo actua, si es menor busca en el hijo izquierdo
            return self._obtener(clave,nodoActual.hijoIzquierdo)
        else: #sino, busca en el hijo derecho
            return self._obtener(clave,nodoActual.hijoDerecho)
    
    def obtener_claves(self): #obtiene una lista con todas las claves de todo el árbol
        claves = [] #inicia una lista vacía
        self._obtener_claves(self.raiz, claves) #llama a _obtener_claves 
        return claves #devuelve lista de claves

    def _obtener_claves(self, nodoActual, claves): #recursividad para buscar claves y añadirlas a la lista
        if nodoActual: #si el nodo actual no es None
            self._obtener_claves(nodoActual.hijoIzquierdo, claves)  # Recorrer el hijo izquierdo
            claves.append(nodoActual.clave)  # Añadir la clave del nodo actual a la lista
            self._obtener_claves(nodoActual.hijoDerecho, claves)  # Recorrer el hijo derecho

    def obtener_lista(self): #obtiene una lista de todos los nodos del árbol ordenados por clave
        return [self.obtener(clave) for clave in self.obtener_claves()]

    def __getitem__(self,clave): #obtiene un valor a partir de una clave dada
        res = self.obtener(clave) #llama a obtener() para obtener el valor de la clave dada
        if res: #si encuentra la clave..
            return res #devuelve el valor de la misma
        else: #si no...
            raise KeyError('Error, la clave no está en el árbol') #muestra que la clave no existe en el árbol

    def __contains__(self,clave): #devuelve True si la clave se encuentra en el árbol
        if self._obtener(clave,self.raiz):
            return True
        else:
            return False

    def longitud(self): #devuelve el tamaño del árbol
        return self.tamano

    def __len__(self): #devuelve el tamaño del árbol (no entendemos por qué está de nuevo)
        return self.tamano

    def __iter__(self):
        return self.raiz.__iter__()

    def eliminar(self,clave):
        if self.tamano > 1: #si el tamaño del árbol es mayor a 1
            nodoAEliminar = self._obtener(clave,self.raiz) #se llama a _obtener() con la clave del nodo a eliminar
            if nodoAEliminar: #si encontro el nodo a eliminar
                self.remover(nodoAEliminar) #efectivamente se elimina
                self.tamano = self.tamano-1 #se reduce el tamaño del arbol -1
            else: #si no encuentra el nodo con la clave dada
                raise KeyError('Error, la clave no está en el árbol') #se avisa que la clave no esta en el árbol
        elif self.tamano == 1 and self.raiz.clave == clave: #si sólo existe un nodo y la clave dada coincide
            self.raiz = None #el árbol queda sin raíz
            self.tamano = self.tamano - 1 #se reduce el tamaño del árbol -1
        else: #sino
            raise KeyError('Error, la clave no está en el árbol') #avisa que la clave no está en el árbol

    def __delitem__(self,clave): #elimina nodo con clave
        self.eliminar(clave)

    def remover(self,nodoActual):#remover nodos según sus conexiones
        if nodoActual.esHoja(): #hoja es cuando no tiene hijos
            if nodoActual == nodoActual.padre.hijoIzquierdo: #si nodo es hijo izquierdo
                nodoActual.padre.hijoIzquierdo = None  #lo desconecta del padre
            else:
                nodoActual.padre.hijoDerecho = None #nodo es hijo derecho y desconecta del padre
        elif nodoActual.tieneAmbosHijos(): #si nodo actual tiene ambos hijos
            suc = nodoActual.encontrarSucesor()#encuentra sucesor
            suc.empalmar() #reemplaza por sus hijos
            nodoActual.clave = suc.clave #reemplaza la clave
            nodoActual.cargaUtil = suc.cargaUtil

        else: # este nodo tiene un (1) hijo
            if nodoActual.tieneHijoIzquierdo(): #si tiene hijo izquierdo
                if nodoActual.esHijoIzquierdo(): #si nodo actual es hijo izquierdo
                    nodoActual.hijoIzquierdo.padre = nodoActual.padre # Actualiza el padre del hijo izquierdo 
                elif nodoActual.esHijoDerecho(): #si tiene hijo derecho
                    nodoActual.hijoIzquierdo.padre = nodoActual.padre #si nodo actual es hijo izquierdo
                    nodoActual.padre.hijoDerecho = nodoActual.hijoIzquierdo #actualiza padre de hijo izquierdo
                else: #si el nodo actual es raíz, reemplaza los datos de nodo actual
                    nodoActual.reemplazarDatoDeNodo(nodoActual.hijoIzquierdo.clave, nodoActual.hijoIzquierdo.cargaUtil, nodoActual.hijoIzquierdo.hijoIzquierdo, nodoActual.hijoIzquierdo.hijoDerecho)
            else: #si tiene hijo derecho
                if nodoActual.esHijoIzquierdo(): #si nodo actual es hijo izquiedo
                    nodoActual.hijoDerecho.padre = nodoActual.padre #actualiza ehijo derecho y enlaza al padrre
                    nodoActual.padre.hijoIzquierdo = nodoActual.hijoDerecho
                elif nodoActual.esHijoDerecho():#si nodo actual es hijo izquierdo
                    nodoActual.hijoDerecho.padre = nodoActual.padre#actualiza hijo derecho y enlaza al padre
                    nodoActual.padre.hijoDerecho = nodoActual.hijoDerecho
                else: # Si el nodo es la raíz, reemplaza los datos con los del hijo derecho.
                    nodoActual.reemplazarDatoDeNodo(nodoActual.hijoDerecho.clave, nodoActual.hijoDerecho.cargaUtil, nodoActual.hijoDerecho.hijoIzquierdo, nodoActual.hijoDerecho.hijoDerecho)

    def inorden(self):
        self._inorden(self.raiz) #llama a la función _inorden

    def _inorden(self,arbol):
        if arbol != None: #si el nodo no es None
            self._inorden(arbol.hijoIzquierdo) #primero visita hijo izquierdo
            print(arbol.clave) #imprime la clave
            self._inorden(arbol.hijoDerecho) #visita hijo derecho

    def postorden(self):
        self._postorden(self.raiz) #llama a _postorden

    def _postorden(self, arbol):
        if arbol: #si no es None
            self._postorden(arbol.hijoDerecho) #visita hijo izquierdo
            self._postorden(arbol.hijoIzquierdo) #visita hijo derecho
            print(arbol.clave) #imprime clave del nodo actual

    def preorden(self):
        self._preorden(self.raiz) #llama a _preorden

    def _preorden(self,arbol):
        if arbol: #si el nodo no es None
            print(arbol.clave) #imprime clave de nodo actual
            self._preorden(arbol.hijoIzquierdo) #visita hijo izquierdo
            self._preorden(arbol.hijoDerecho) #visita hijo derecho


#la clase ABB usa instancias de la clase NodoArbol para irse creando. cada nodo es una insatncia de la clase
class NodoArbol: #raiz del ABB. define la estructura básica para crear un nodo del ABB
    def __init__(self,clave,valor,izquierdo=None,derecho=None,padre=None): #constructor con parámetros clave, valor, izquierdo,derecho y padre apuntando a None por defecto
        self.clave = clave 
        self.cargaUtil = valor
        self.hijoIzquierdo = izquierdo #apunta al nodo hijo que esta a la izquierda
        self.hijoDerecho = derecho #apunta al nodo hijo que esta a la derecha
        self.padre = padre #apunta al nodo padre
        self.factorEquilibrio = 0 #inicailiza la variable en 0 que se usa para mantener equilibrado el ABB

    def tieneHijoIzquierdo(self): 
        return self.hijoIzquierdo #devuelve la clave del hijo izquierdo

    def tieneHijoDerecho(self):
        return self.hijoDerecho #devuelve la clave del hijo izquierdo

    def esHijoIzquierdo(self): #responde a ¿soy el izquierdo de mi padre? funcion que sirve conectar correctamente un hijo con su padre si se elimina un nodo
        return self.padre and self.padre.hijoIzquierdo == self # se fija si el nodo actual tiene padre y si el nodo izquierdo del padre es el nodo actual

    def esHijoDerecho(self): #devuelve bool. Se fija si el nodo derecho es hijo del padre
        return self.padre and self.padre.hijoDerecho == self #se fija si tiene nodo padre y si el nodo derecho del padre es el nodo actual

    def esRaiz(self): #devuelve Bool. Nodo raiz es el nodo que no tiene aristas
        return not self.padre #si tiene padre devuelve False, es decir que si tiene padre entonces tiene aristas y por lo tanto no es nodo raiz x su definición

    def esHoja(self): #devuelve Bool. Es hoja si no tiene hijos. si no es hoja devuelve True
        return not (self.hijoDerecho or self.hijoIzquierdo) #niega el booleanoo de fijarse si tiene hijo derecho o izquierdo

    def tieneAlgunHijo(self): #Devuelve booleano
        return self.hijoDerecho or self.hijoIzquierdo #se fija si tiene hijo izquierdo o derecho

    def tieneAmbosHijos(self): #Devuelve bool. 
        return self.hijoDerecho and self.hijoIzquierdo #se fija si tiene ambos hijos

    def reemplazarDatoDeNodo(self,clave,valor,hizq,hder): #sirve para cambiar valores de clave, valor, hizq y hder
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = hizq
        self.hijoDerecho = hder
        if self.tieneHijoIzquierdo(): #si existe el hijo izquierdo
            self.hijoIzquierdo.padre = self #se lo establece como hijo izquierdo del padre 
        if self.tieneHijoDerecho(): #si existe hijo derecho
            self.hijoDerecho.padre = self #se lo establece como hijo derecho del padre

    def encontrarSucesor(self): #remplaza el nodo actual por el nodo con la menor clave en el subarbol derecho. Elimina el nodo actual y mantiene el orden de los demas nodos
        suc = None #crea variable
        if self.tieneHijoDerecho(): #si tiene hijo derecho
            suc = self.hijoDerecho.encontrarMin() #asigna a la variable el ressultado de encontrar el minimo en los nodos derecho
        else: #si no tiene hijo derecho
            if self.padre: #si nodo actual tiene padre
                if self.esHijoIzquierdo(): #si nodo actual es hijo izquierdo
                    suc = self.padre #el nodo mayor de los izquierdo es el padre y por lo tanto el suc sera el padre
                else: #si es el hijo derecho
                    self.padre.hijoDerecho = None #hijo derecho del padre aputa a NOne. Lo desconecta de su padre
                    suc = self.padre.encontrarSucesor() #busca recursivamente el sucesor del padre
                    self.padre.hijoDerecho = self #conecta el nodo actual a su padre
        return suc #devuelve el sucesor

    def empalmar(self): #elimina el nodo actual y conecta a los hijos al padre
        if self.esHoja(): #si el nodo actual no tiene hijos
            if self.esHijoIzquierdo(): #si el actual es el hijo izquierdo
                self.padre.hijoIzquierdo = None #lo elimina apuntando directo el padre a None
            else: #si es el hijo derecho del padre
                self.padre.hijoDerecho = None #el derecho del pare apunta a None
        elif self.tieneAlgunHijo(): #si tiene hijo
            if self.tieneHijoIzquierdo(): #si el nodo actual tiene hijo izquierdo
                if self.esHijoIzquierdo(): ##y si el nodo actual tambien es el hijo izquierdo
                    self.padre.hijoIzquierdo = self.hijoIzquierdo #se actualiza el hijo izquierdo del padre
                else: #si no tiene hijo izquierdo
                    self.padre.hijoDerecho = self.hijoIzquierdo #entonces el izquierdo ahora pasa a ser el derecho del padre
                self.hijoIzquierdo.padre = self.padre #el padre será el izquierdo del padre
            else: #si es hijo derecho
                if self.esHijoIzquierdo(): #si es izquierdo del derecho
                    self.padre.hijoIzquierdo = self.hijoDerecho #el hijo derecho del nodo actual será el hijo izquierdo del padre
                else: #si es hijo derecho
                    self.padre.hijoDerecho = self.hijoDerecho #el hijo derecho del nodo actual, será el hijo derecho del padre
                self.hijoDerecho.padre = self.padre #el padre del actual sera el hijo derecho del padre

    def encontrarMin(self): #encuentra el nodo con la menor clave en el subarbol
        actual = self #inicializa la variable actual al actual
        while actual.tieneHijoIzquierdo(): #mietras actual tenga hijo izquierdo
            actual = actual.hijoIzquierdo #itera sobre el actual y actualiz la variable
        return actual #devuelve el nodo actual

    def __iter__(self): #itera los nodos de modo inorden
        if self: #si tiene nodo
            if self.tieneHijoIzquierdo(): #si tiene hijo izquierdo
                for elem in self.hijoIzquierdo: #recorre los elementos izquierdo
                    yield elem #yield pausa la ejecución mostrando un valor
            yield self.clave #define que el valor sera el próximo elemento de la iteración 
            if self.tieneHijoDerecho(): #si el actual tiene hijo derecho
                for elem in self.hijoDerecho: #recorre elementos derechos
                    yield elem #yield pausa la ejecución mostrando un valor