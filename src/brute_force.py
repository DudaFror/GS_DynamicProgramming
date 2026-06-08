class BruteForceSearch:

    def __init__(self, graph):
        self.graph = graph

        self.best_path = None
        self.best_cost = float("inf")

        self.recursive_calls = 0
        self.paths_evaluated = 0