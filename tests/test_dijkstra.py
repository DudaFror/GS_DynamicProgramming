from src.data_structures import Graph
from src.greedy import Dijkstra


graph = Graph()

graph.add_edge("A", "B", 2)
graph.add_edge("A", "C", 5)
graph.add_edge("B", "D", 4)
graph.add_edge("C", "D", 1)

dijkstra = Dijkstra(graph)

path, cost = dijkstra.shortest_path(
    "A",
    "D"
)

print("Caminho:", path)
print("Custo:", cost)