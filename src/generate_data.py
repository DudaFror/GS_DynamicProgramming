import random

from src.data_structures import Graph


def generate_graph(
    num_vertices,
    max_weight=20
):

    graph = Graph()

    vertices = [
        f"V{i}"
        for i in range(num_vertices)
    ]

    # Garantir conectividade

    for i in range(num_vertices - 1):

        weight = random.randint(
            1,
            max_weight
        )

        graph.add_edge(
            vertices[i],
            vertices[i + 1],
            weight
        )

    # Adicionar conexões extras

    extra_edges = num_vertices

    for _ in range(extra_edges):

        source = random.choice(vertices)
        destination = random.choice(vertices)

        if source != destination:

            weight = random.randint(
                1,
                max_weight
            )

            graph.add_edge(
                source,
                destination,
                weight
            )

    return graph

if __name__ == "__main__":

    graph = generate_graph(5)

    graph.display()

TEST_SIZES = [
    5,
    8,
    10,
    12,
    20,
    50,
    100
]