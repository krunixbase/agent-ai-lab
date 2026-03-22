import time
import logging

logger = logging.getLogger(__name__)

def measure_time(func):
    """Decorator that logs execution time of a function."""
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        duration = (time.perf_counter() - start) * 1000
        logger.debug(f"{func.__name__} executed in {duration:.2f} ms")
        return result
    return wrapper
