import heapq

class Graph:
    def __init__(self):
        self.edges = {}
        self.vertices = set()

    def add_edge(self, u, v, weight):
        if u not in self.edges:
            self.edges[u] = []
        if v not in self.edges:
            self.edges[v] = []
        self.edges[u].append((v, weight))
        self.edges[v].append((u, weight))  # Якщо граф ненаправлений
        self.vertices.add(u)
        self.vertices.add(v)

def dijkstra(graph, start):
    # Відстані до всіх вершин
    distances = {vertex: float('infinity') for vertex in graph.vertices}
    distances[start] = 0

    # Пріоритетна черга для вибору вершини з найменшою відстанню
    priority_queue = [(0, start)]
    heapq.heapify(priority_queue)

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph.edges[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Приклад використання
graph = Graph()
graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 4)
graph.add_edge('B', 'C', 2)
graph.add_edge('B', 'D', 5)
graph.add_edge('C', 'D', 1)

start_vertex = 'A'
distances = dijkstra(graph, start_vertex)

print(f"Відстані від вершини {start_vertex}:")
for vertex in distances:
    print(f"До вершини {vertex}: {distances[vertex]}")