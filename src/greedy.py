import heapq


class Dijkstra:

    def __init__(self, graph):
        self.graph = graph

    def shortest_path(self, start, end):

        distances = {
            vertex: float("inf")
            for vertex in self.graph.graph
        }

        previous = {}

        distances[start] = 0

        priority_queue = [(0, start)]

        while priority_queue:

            current_distance, current_vertex = heapq.heappop(
                priority_queue
            )

            if current_vertex == end:
                break

            for neighbor, weight in self.graph.get_neighbors(
                current_vertex
            ):

                distance = (
                    current_distance + weight
                )

                if distance < distances[neighbor]:

                    distances[neighbor] = distance

                    previous[neighbor] = current_vertex

                    heapq.heappush(
                        priority_queue,
                        (
                            distance,
                            neighbor
                        )
                    )

        return self._reconstruct_path(
            previous,
            start,
            end
        ), distances[end]  

    def _reconstruct_path(
        self,
        previous,
        start,
        end
    ):

        path = []

        current = end

        while current != start:

            path.append(current)

            current = previous.get(current)

            if current is None:
                return []

        path.append(start)

        path.reverse()

        return path