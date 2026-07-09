import math
import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        # The solution will be like: {destination, distance}, so it will be n-1 long (minus src)

        # 1. Construir la Lista de Adyacencia desde la Lista de Aristas (Edge List)
        # Inicializamos un diccionario vacío para cada uno de los 'n' nodos
        grafo: dict[int, list[tuple[int, int]]] = {i: [] for i in range(n)}
        shortestPath = []

        for origen, destino, peso in edges:
            # Guardamos la tupla como (peso, destino).
            # El peso va primero para que el Min-Heap ordene automáticamente por coste.
            grafo[origen].append((peso, destino))

        # 2. Inicializar la tabla de distancias con Infinito (math.inf)
        distancias = {nodo: math.inf for nodo in range(n)}
        distancias[src] = 0  # La distancia al nodo origen es 0

        visitados = set()

        cola_prioridad = [(0, src)]

        while cola_prioridad:
            # Extraemos el nodo con el menor coste acumulado actual -> O(log V)
            distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)

            # Si el nodo ya fue visitado por un camino más corto, lo ignoramos
            if nodo_actual in visitados:
                continue

            # Marcamos el nodo actual como visitado definitivamente
            visitados.add(nodo_actual)

            # 5. Relajación de aristas: Exploramos los vecinos del nodo actual
            for peso_arista, vecino in grafo[nodo_actual]:
                if vecino in visitados:
                    continue

                nueva_distancia = distancia_actual + peso_arista

                # Si encontramos un camino más corto hacia el vecino, actualizamos la tabla
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    # Metemos el vecino en el heap con su nueva prioridad -> O(log V)
                    heapq.heappush(cola_prioridad, (nueva_distancia, vecino))

        
        # Cambiar inf por -1
        for nodo in distancias:
            if distancias[nodo] == math.inf:
                distancias[nodo] = -1

        return distancias
             