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
    compare_algorithms,
    PerformanceMonitor
)

from src.results_exporter import (
    export_results
)


results = []

for size in TEST_SIZES:

    print(f"\nExecutando benchmark N={size}")

    graph = generate_graph(size)

    vertices = list(graph.graph.keys())

    start = vertices[0]
    end = vertices[-1]

    dijkstra = Dijkstra(graph)

    # Força Bruta apenas para instâncias pequenas
    if size <= 12:

        brute_force = BruteForceSearch(graph)

        comparison = compare_algorithms(
            brute_force,
            dijkstra,
            start,
            end
        )

        brute_time = comparison[
            "brute_force"
        ][
            "execution_time_ms"
        ]

        dijkstra_time = comparison[
            "dijkstra"
        ][
            "execution_time_ms"
        ]

    else:

        brute_time = None

        dijkstra_metrics = PerformanceMonitor.measure(
            dijkstra.shortest_path,
            start,
            end
        )

        dijkstra_time = dijkstra_metrics[
            "execution_time_ms"
        ]

    results.append(
        (
            size,
            round(brute_time, 3)
            if brute_time is not None
            else "N/A",
            round(dijkstra_time, 3)
        )
    )

export_results(
    "benchmark_results.csv",
    results
)

print("\nBenchmark finalizado!")