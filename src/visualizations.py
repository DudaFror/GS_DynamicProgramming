import networkx as nx
import matplotlib.pyplot as plt


def plot_graph(graph):

    G = nx.Graph()

    for source in graph.graph:

        for destination, weight in graph.graph[source]:

            G.add_edge(
                source,
                destination,
                weight=weight
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
        node_size=2000
    )

    edge_labels = nx.get_edge_attributes(
        G,
        "weight"
    )

    nx.draw_networkx_edge_labels(
        G,
        pos,
        edge_labels=edge_labels
    )

    plt.title(
        "Grafo de Municípios"
    )

    plt.show()

    def plot_execution_times(
        sizes,
        brute_force_times,
        dijkstra_times
    ):

        plt.figure(figsize=(10, 6))

        plt.plot(
            sizes,
            brute_force_times,
            marker="o",
            label="Força Bruta"
        )

        plt.plot(
            sizes,
            dijkstra_times,
            marker="o",
            label="Dijkstra"
        )

        plt.xlabel("Número de vértices")

        plt.ylabel(
            "Tempo (ms)"
        )

        plt.title(
            "Tempo de Execução x Número de Vértices"
        )

        plt.legend()

        plt.grid(True)

        plt.show()