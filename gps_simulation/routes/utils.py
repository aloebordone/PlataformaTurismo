import heapq
from .models import City, Route

def dijkstra(start_city): #algoritmo de dijkstra para calcular las distancias más cortas para ir de una ciudad a otra
    distances = {start_city:0} #abre un diccionario para las distancias, que inicia en 0
    previous_cities = {start_city:None} #diccionario para rastrear la ciudad anterior
    # completar
    return distances, previous_cities #devuelve los dos diccionarios de distancias y ciudades anteriores

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

class NodoArbol:
    def __init__(self,clave,valor,izquierdo=None,derecho=None,padre=None):
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = izquierdo
        self.hijoDerecho = derecho
        self.padre = padre
        self.factorEquilibrio = 0

    def tieneHijoIzquierdo(self):
        return self.hijoIzquierdo

    def tieneHijoDerecho(self):
        return self.hijoDerecho

    def esHijoIzquierdo(self):
        return self.padre and self.padre.hijoIzquierdo == self

    def esHijoDerecho(self):
        return self.padre and self.padre.hijoDerecho == self

    def esRaiz(self):
        return not self.padre

    def esHoja(self):
        return not (self.hijoDerecho or self.hijoIzquierdo)

    def tieneAlgunHijo(self):
        return self.hijoDerecho or self.hijoIzquierdo

    def tieneAmbosHijos(self):
        return self.hijoDerecho and self.hijoIzquierdo

    def reemplazarDatoDeNodo(self,clave,valor,hizq,hder):
        self.clave = clave
        self.cargaUtil = valor
        self.hijoIzquierdo = hizq
        self.hijoDerecho = hder
        if self.tieneHijoIzquierdo():
            self.hijoIzquierdo.padre = self
        if self.tieneHijoDerecho():
            self.hijoDerecho.padre = self

    def encontrarSucesor(self):
        suc = None
        if self.tieneHijoDerecho():
            suc = self.hijoDerecho.encontrarMin()
        else:
            if self.padre:
                if self.esHijoIzquierdo():
                    suc = self.padre
                else:
                    self.padre.hijoDerecho = None
                    suc = self.padre.encontrarSucesor()
                    self.padre.hijoDerecho = self
        return suc

    def empalmar(self):
        if self.esHoja():
            if self.esHijoIzquierdo():
                self.padre.hijoIzquierdo = None
            else:
                self.padre.hijoDerecho = None
        elif self.tieneAlgunHijo():
            if self.tieneHijoIzquierdo():
                if self.esHijoIzquierdo():
                    self.padre.hijoIzquierdo = self.hijoIzquierdo
                else:
                    self.padre.hijoDerecho = self.hijoIzquierdo
                self.hijoIzquierdo.padre = self.padre
            else:
                if self.esHijoIzquierdo():
                    self.padre.hijoIzquierdo = self.hijoDerecho
                else:
                    self.padre.hijoDerecho = self.hijoDerecho
                self.hijoDerecho.padre = self.padre

    def encontrarMin(self):
        actual = self
        while actual.tieneHijoIzquierdo():
            actual = actual.hijoIzquierdo
        return actual

    def __iter__(self):
        if self:
            if self.tieneHijoIzquierdo():
                for elem in self.hijoIzquierdo:
                    yield elem
            yield self.clave
            if self.tieneHijoDerecho():
                for elem in self.hijoDerecho:
                    yield elem