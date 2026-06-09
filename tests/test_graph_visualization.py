from src.data_structures import Graph
from src.visualizations import plot_graph


graph = Graph()

graph.add_edge("Manaus", "Coari", 10)
graph.add_edge("Manaus", "Tefe", 15)
graph.add_edge("Coari", "Tefe", 5)

plot_graph(graph)

