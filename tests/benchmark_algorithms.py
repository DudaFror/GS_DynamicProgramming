from src.generate_data import (
    generate_graph,
    TEST_SIZES
)

from src.brute_force import (
    BruteForceSearch
)

from src.greedy import (
    Dijkstra
)

from src.performance_monitor import (
    compare_algorithms
)


for size in TEST_SIZES:

    print(f"\nExecutando N={size}")

    graph = generate_graph(size)

    vertices = list(graph.graph.keys())

    start = vertices[0]
    end = vertices[-1]

    brute_force = BruteForceSearch(graph)

    dijkstra = Dijkstra(graph)

    result = compare_algorithms(
        brute_force,
        dijkstra,
        start,
        end
    )

    print(result)