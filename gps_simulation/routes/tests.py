import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gps_simulation.settings") #configuramos el entorno de django
django.setup()


from django.test import TestCase

# Create your tests here.

from .models import City, Route
from .utils import get_shortest_path  # Ajusta el import según mi estructura de proyecto

class DijkstraAlgorithmTest(TestCase):
    def setUp(self): 
        #crea ciudades
        self.rg = City.objects.create(name="RG")  # Río Gallegos
        self.ec = City.objects.create(name="EC")  #El Chaltén
        self.pt = City.objects.create(name="PT")  #Pico Truncado
        self.co = City.objects.create(name="CO")  #Caleta Olivia
        self.lh = City.objects.create(name="LH")  #Las Heras
        self.pm = City.objects.create(name="PM")  #Perito Moreno
        self.la = City.objects.create(name="LA")  #Los Antiguos
        self.eca = City.objects.create(name="ECA")  #El Calafate
        
        #crea rutas
        Route.objects.create(start_city=self.rg, end_city=self.ec, distance=450.0)
        Route.objects.create(start_city=self.rg, end_city=self.pt, distance=687.0)
        Route.objects.create(start_city=self.rg, end_city=self.co, distance=700.0)
        Route.objects.create(start_city=self.rg, end_city=self.lh, distance=768.0)
        Route.objects.create(start_city=self.rg, end_city=self.pm, distance=936.0)
        Route.objects.create(start_city=self.rg, end_city=self.la, distance=993.0)
        Route.objects.create(start_city=self.rg, end_city=self.eca, distance=305.0)

        # Agrega rutas directas adicionales entre otras ciudades
        Route.objects.create(start_city=self.ec, end_city=self.pm, distance=131.0)
        Route.objects.create(start_city=self.co, end_city=self.lh, distance=135.0)
        Route.objects.create(start_city=self.pt, end_city=self.la, distance=307.0)
        Route.objects.create(start_city=self.ec, end_city=self.eca, distance=213.0)
        Route.objects.create(start_city=self.eca, end_city=self.la, distance=687.0)
     
    def test_direct_route(self):
    #Prueba una ruta directa donde no se necesita pasar por otra ciudad
        path, distance = get_shortest_path(self.ec, self.eca)
        expected_path = [self.ec, self.eca]
        expected_distance = 213.0
        self.assertEqual(path, expected_path)
        self.assertEqual(distance, expected_distance)
    
    def test_multiple_routes(self): #creamos una ruta más larga y vemos si sigue dando la más corta
        Route.objects.create(start_city=self.co, end_city=self.eca, distance=320.0)
        path, distance = get_shortest_path(self.rg, self.eca)
        expected_distance = 305.0  # para ver si sigue usando la ruta más corta
        self.assertEqual(distance, expected_distance)

    def test_same_city(self): #si pongo la misma ciudad me tiene que dar 0
        path, distance = get_shortest_path(self.rg, self.rg)
        self.assertEqual(distance, 0)
        self.assertEqual(path, [self.rg])

    def test_indirect_route(self):
        path, distance = get_shortest_path(self.rg, self.la)  #la ruta directa era de 993 km, pero pasando por el calafate da 992
        expected_distance = 992.0
        expected_path = [self.rg, self.eca, self.la]  #ciudades por las que pasaría
        self.assertEqual(distance, expected_distance)
        self.assertEqual([city.name for city in path], [city.name for city in expected_path])
