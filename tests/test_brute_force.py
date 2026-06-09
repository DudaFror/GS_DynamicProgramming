from src.data_structures import Graph
from src.brute_force import BruteForceSearch

graph = Graph()

graph.add_edge("A", "B", 2)
graph.add_edge("A", "C", 5)
graph.add_edge("B", "D", 4)
graph.add_edge("C", "D", 1)

brute_force = BruteForceSearch(graph)

path, cost = brute_force.find_best_path(
    "A",
    "D"
)

print("Melhor caminho:", path)
print("Custo:", cost)