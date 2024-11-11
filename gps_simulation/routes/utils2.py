"""from heapq import heappush, heappop"""

"""def dijkstra(graph, start_city):"""
"""
  Calcula la ruta más corta desde una ciudad inicial a todas las demás ciudades en el grafo.

  Args:
      graph: Un diccionario donde las claves son las ciudades y los valores son listas de tuplas (ciudad vecina, distancia).
      start_city: La ciudad inicial para la que se calcula la ruta más corta.

  Returns:
      Un diccionario con dos claves:
          'distances': Un diccionario donde las claves son las ciudades y los valores son las distancias más cortas desde la ciudad inicial.
          'previous': Un diccionario donde las claves son las ciudades y los valores son las ciudades anteriores en la ruta más corta.
  """
"""distances = {city: float('inf') for city in graph}
  distances[start_city] = 0
  previous = {city: None for city in graph}
  priority_queue = [(0, start_city)]"""

"""while priority_queue:
    current_distance, current_city = heappop(priority_queue)

    if current_distance > distances[current_city]:
      continue

    for neighbor, distance_to_neighbor in graph[current_city]:
      new_distance = current_distance + distance_to_neighbor
      if new_distance < distances[neighbor]:
        distances[neighbor] = new_distance
        previous[neighbor] = current_city
        heappush(priority_queue, (new_distance, neighbor))

  return distances, previous"""