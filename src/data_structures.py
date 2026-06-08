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

class Node:
    def __init__(self, municipality):
        self.municipality = municipality
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, municipality):
        if self.root is None:
            self.root = Node(municipality)
        else:
            self._insert(self.root, municipality)

    def _insert(self, current, municipality):
        risk = municipality[2]

        if risk < current.municipality[2]:
            if current.left is None:
                current.left = Node(municipality)
            else:
                self._insert(current.left, municipality)

        else:
            if current.right is None:
                current.right = Node(municipality)
            else:
                self._insert(current.right, municipality)

if __name__ == "__main__":

    bst = BinarySearchTree()

    bst.insert((1, "Manaus", 0.92, 120, 2200000))
    bst.insert((2, "Tefe", 0.60, 80, 65000))
    bst.insert((3, "Coari", 0.75, 90, 90000))

    print("BST criada com sucesso!")