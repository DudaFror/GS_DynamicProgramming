import time
import tracemalloc


class PerformanceMonitor:

    @staticmethod
    def measure(algorithm, *args):

        tracemalloc.start()

        start_time = time.perf_counter()

        result = algorithm(*args)

        end_time = time.perf_counter()

        current_memory, peak_memory = tracemalloc.get_traced_memory()

        tracemalloc.stop()

        return {
            "result": result,
            "execution_time_ms": (
                end_time - start_time
            ) * 1000,
            "peak_memory_kb": peak_memory / 1024
        }
    
    def compare_algorithms(
        brute_force,
        dijkstra,
        start,
        end
    ):

        brute_metrics = PerformanceMonitor.measure(
            brute_force.find_best_path,
            start,
            end
        )

        dijkstra_metrics = PerformanceMonitor.measure(
            dijkstra.shortest_path,
            start,
            end
        )

        return {
            "brute_force": brute_metrics,
            "dijkstra": dijkstra_metrics
        }