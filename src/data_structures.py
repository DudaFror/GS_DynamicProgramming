class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.graph:
            self.graph[vertex_id] = []

    def add_edge(self, source, destination, weight):
        self.add_vertex(source)
        self.add_vertex(destination)

        self.graph[source].append((destination, weight))
        self.graph[destination].append((source, weight))

    def get_neighbors(self, vertex):
        return self.graph.get(vertex, [])

    def display(self):
        for vertex, neighbors in self.graph.items():
            print(f"{vertex} -> {neighbors}")

if __name__ == "__main__":
    g = Graph()

    g.add_edge("Manaus", "Itacoatiara", 150)
    g.add_edge("Manaus", "Parintins", 350)

    g.display()