from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import networkx as nx
from .models import City, Route
from .utils import get_shortest_path, ArbolBinarioBusqueda

# routes/views.py
def home(request):
    # Obtener todas las ciudades de la base de datos
    ciudades = City.objects.all()
    # Pasar las ciudades al template para que se muestren
    # implementar un abb de la cuidad y pasarlo al template
    arbol_ciudades = ArbolBinarioBusqueda()
    for ciudad in ciudades:
        arbol_ciudades.agregar(ciudad.name,ciudad)
    return render(request, 'routes/home.html', {'ciudades': arbol_ciudades.obtener_lista()})

def shortest_route(request):
    ciudades = City.objects.all()
    if request.method == 'POST':
        start_city = get_object_or_404(City, id=request.POST.get('start_city'))
        end_city = get_object_or_404(City, id=request.POST.get('end_city'))
        path, distance = get_shortest_path(start_city, end_city)
        return render(request, 'routes/shortest_route_form.html', {
            'ciudades': ciudades,
            'path': path,
            'distance': distance,
        })
    return render(request, 'routes/shortest_route_form.html', {'ciudades': ciudades})

def load_graph(request):
    if request.method == 'POST':
        # Verifica si se subió texto
        if 'graph_text' in request.POST and request.POST['graph_text'].strip():
            graph_data = request.POST['graph_text'].strip()
        else:
            return render(request, 'routes/load_graph.html', {
                'error_message': 'Please upload a file or enter graph data.'
            })

        try:
            # Procesa los datos para construir el grafo
            graph = nx.parse_edgelist(graph_data.splitlines(), nodetype=int, data=(('weight', float),))
            # Para cada arista del grafo, verifica si las ciudades existen y crea las rutas
            ciudades_existentes = City.objects.all()
            ciudades_dict = {ciudad.id: ciudad for ciudad in ciudades_existentes}
            
            rutas_creadas = []
            rutas_actualizadas = []
            rutas_error = []
            
            for edge in graph.edges(data=True):
                start_id, end_id, attributes = edge
                distancia = attributes.get('weight', 0)
                
                # Verificar si los IDs de las ciudades existen
                if start_id in ciudades_dict and end_id in ciudades_dict:
                    start_city = ciudades_dict[start_id]
                    end_city = ciudades_dict[end_id]
                    
                    # Crear o actualizar la ruta entre las ciudades
                    route, created = Route.objects.update_or_create(
                        start_city=start_city, 
                        end_city=end_city, 
                        defaults={'distance': distancia}
                    )
                    
                    if created:
                        rutas_creadas.append(f"{start_city.name} -> {end_city.name} ({distancia} km)")
                    else:
                        rutas_actualizadas.append(f"Route updated: {start_city.name} -> {end_city.name} ({distancia} km)")
                else:
                    rutas_error.append(f"Cities with IDs {start_id} or {end_id} do not exist in the system")
            
            return render(request, 'routes/load_graph.html', {
                'success_message': f'Información procesada con éxito! {len(rutas_creadas)} rutas creadas.',
                'error_message': f"{len(rutas_error)} rutas no fueron creadas",
                'rutas_creadas': rutas_creadas,
                'rutas_error': rutas_error,
            })

        except Exception as e:
            return render(request, 'routes/load_graph.html', {
                'error_message': f'Error loading graph: {e}'
            })

    return render(request, 'routes/load_graph.html')

from django.shortcuts import render, get_object_or_404
from .models import City, Route

def city_detail(request, id):
    # Obtener la ciudad por ID o mostrar 404 si no existe
    ciudad = get_object_or_404(City, id=id)

    # Obtener todas las rutas que comienzan o terminan en esta ciudad
    rutas_salida = Route.objects.filter(start_city=ciudad)
    rutas_llegada = Route.objects.filter(end_city=ciudad)

    return render(request, 'routes/city_detail.html', {
        'ciudad': ciudad,
        'rutas_salida': rutas_salida,
        'rutas_llegada': rutas_llegada
    })


"""Ejemplo Simplificado para crear un grafo de ruta mas corta usando el algoritmo djistra(views.py):

Python
import networkx as nx
from .models import Ciudad, Conexion

def encontrar_ruta(request, origen, destino):
    # Construir el grafo
    G = nx.Graph()
    for conexion in Conexion.objects.all():
        G.add_edge(conexion.origen.id, conexion.destino.id, weight=conexion.distancia)

    try:
        ruta = nx.dijkstra_path(G, origen, destino, weight='weight')
        return render(request, 'ruta.html', {'ruta': ruta})
    except nx.NetworkXNoPath:
        return render(request, 'ruta.html', {'error': 'No se encontró ruta'})"""
