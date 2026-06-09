from src.data_structures import Graph
from src.brute_force import BruteForceSearch
from src.greedy import Dijkstra
from src.performance_monitor import compare_algorithms


graph = Graph()

graph.add_edge("A", "B", 2)
graph.add_edge("A", "C", 5)
graph.add_edge("B", "D", 4)
graph.add_edge("C", "D", 1)

bf = BruteForceSearch(graph)
dj = Dijkstra(graph)

result = compare_algorithms(
    bf,
    dj,
    "A",
    "D"
)

print(result)