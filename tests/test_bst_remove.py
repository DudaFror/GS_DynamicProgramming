from src.data_structures import (
    BinarySearchTree
)

bst = BinarySearchTree()

bst.insert((1, "Manaus", 0.92, 120, 2200000))
bst.insert((2, "Tefe", 0.60, 80, 65000))
bst.insert((3, "Coari", 0.75, 90, 90000))

print("Antes:")

print(bst.in_order())

bst.remove(0.75)

print("\nDepois:")

print(bst.in_order())