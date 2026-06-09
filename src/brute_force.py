class BruteForceSearch:

    def __init__(self, graph):
        self.graph = graph

        self.best_path = None
        self.best_cost = float("inf")

        self.recursive_calls = 0
        self.paths_evaluated = 0

    def find_best_path(self, start, end):

        self.best_path = None
        self.best_cost = float("inf")

        self._backtrack(
            start,
            end,
            set(),
            [],
            0
        )

        return self.best_path, self.best_cost
    
    def _backtrack(
        self,
        current,
        destination,
        visited,
        path,
        cost
    ):

        self.recursive_calls += 1

        visited.add(current)
        path.append(current)

        if current == destination:

            self.paths_evaluated += 1

            if cost < self.best_cost:
                self.best_cost = cost
                self.best_path = path.copy()

        else:

            for neighbor, weight in self.graph.get_neighbors(current):

                if neighbor not in visited:

                    self._backtrack(
                        neighbor,
                        destination,
                        visited,
                        path,
                        cost + weight
                    )

        path.pop()
        visited.remove(current)