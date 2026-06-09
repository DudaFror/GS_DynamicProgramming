import csv


def export_results(
    filename,
    results
):

    with open(
        filename,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "N",
            "BruteForce(ms)",
            "Dijkstra(ms)"
        ])

        for row in results:

            writer.writerow(row)