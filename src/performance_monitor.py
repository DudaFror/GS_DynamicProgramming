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