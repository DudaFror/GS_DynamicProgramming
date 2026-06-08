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
    
    def in_order(self):
        result = []
        self._in_order(self.root, result)
        return result


    def _in_order(self, node, result):
        if node is not None:
            self._in_order(node.left, result)
            result.append(node.municipality)
            self._in_order(node.right, result)

    def height(self):
        return self._height(self.root)

    def _height(self, node):

        if node is None:
            return 0

        left_height = self._height(node.left)
        right_height = self._height(node.right)

        return max(left_height, right_height) + 1

    def search_range(self, min_risk, max_risk):
        result = []
        self._search_range(self.root, min_risk, max_risk, result)
        return result


    def _search_range(self, node, min_risk, max_risk, result):

        if node is None:
            return

        risk = node.municipality[2]

        if min_risk <= risk <= max_risk:
            result.append(node.municipality)

        if risk > min_risk:
            self._search_range(
                node.left,
                min_risk,
                max_risk,
                result
            )

        if risk < max_risk:
            self._search_range(
                node.right,
                min_risk,
                max_risk,
                result
            )

# Testes
if __name__ == "__main__":

    bst = BinarySearchTree()

    bst.insert((1, "Manaus", 0.92, 120, 2200000))
    bst.insert((2, "Tefe", 0.60, 80, 65000))
    bst.insert((3, "Coari", 0.75, 90, 90000))

    print("\nMunicipios ordenados por risco:")

    for municipio in bst.in_order():
        print(municipio)
    
    print(f"\nAltura da árvore: {bst.height()}")

    print("\nMunicipios com risco entre 0.70 e 1.00:")

    for municipio in bst.search_range(0.70, 1.00):
        print(municipio)