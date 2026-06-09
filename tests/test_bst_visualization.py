from src.data_structures import BinarySearchTree


def print_tree(node, level=0):

    if node is not None:

        print_tree(
            node.right,
            level + 1
        )

        print(
            "    " * level +
            str(node.municipality[2])
        )

        print_tree(
            node.left,
            level + 1
        )


bst = BinarySearchTree()

bst.insert((1, "Manaus", 0.92, 120, 2200000))
bst.insert((2, "Tefe", 0.60, 80, 65000))
bst.insert((3, "Coari", 0.75, 90, 90000))
bst.insert((4, "Parintins", 0.88, 100, 115000))
bst.insert((5, "Humaita", 0.45, 60, 50000))

print_tree(bst.root)