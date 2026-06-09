from src.data_structures import BinarySearchTree
import matplotlib.pyplot as plt
import networkx as nx


def add_edges(graph, node):

    if node is None:
        return

    risk = node.municipality[2]

    if node.left:

        left_risk = node.left.municipality[2]

        graph.add_edge(
            str(risk),
            str(left_risk)
        )

        add_edges(
            graph,
            node.left
        )

    if node.right:

        right_risk = node.right.municipality[2]

        graph.add_edge(
            str(risk),
            str(right_risk)
        )

        add_edges(
            graph,
            node.right
        )


bst = BinarySearchTree()

bst.insert((1, "Manaus", 0.92, 120, 2200000))
bst.insert((2, "Tefe", 0.60, 80, 65000))
bst.insert((3, "Coari", 0.75, 90, 90000))
bst.insert((4, "Parintins", 0.88, 100, 115000))
bst.insert((5, "Humaita", 0.45, 60, 50000))

G = nx.DiGraph()

add_edges(
    G,
    bst.root
)

plt.figure(figsize=(8, 6))

pos = nx.spring_layout(
    G,
    seed=42
)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=2500
)

plt.title(
    "BST Ordenada por Índice de Risco"
)

plt.savefig(
    "bst_visualization.png"
)

plt.show()