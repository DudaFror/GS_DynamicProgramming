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