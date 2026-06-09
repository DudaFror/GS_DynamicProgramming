import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(
    "benchmark_results.csv"
)

sizes = df["N"]

dijkstra_times = df["Dijkstra(ms)"]

brute_force_times = []

for value in df["BruteForce(ms)"]:

    if value == "N/A":
        brute_force_times.append(None)
    else:
        brute_force_times.append(
            float(value)
        )

plt.figure(figsize=(10, 6))

plt.plot(
    sizes,
    dijkstra_times,
    marker="o",
    label="Dijkstra"
)

plt.plot(
    sizes,
    brute_force_times,
    marker="o",
    label="Força Bruta"
)

plt.title(
    "Tempo de Execução x Número de Vértices"
)

plt.xlabel(
    "Número de Vértices"
)

plt.ylabel(
    "Tempo (ms)"
)

plt.legend()

plt.grid(True)

plt.savefig(
    "execution_times.png"
)

plt.show()  