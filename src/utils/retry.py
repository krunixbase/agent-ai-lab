import time
import logging
from typing import Callable, Type, Tuple

logger = logging.getLogger(__name__)

def retry(
    exceptions: Tuple[Type[BaseException], ...],
    retries: int = 3,
    delay: float = 0.5,
    backoff: float = 2.0,
):
    """
    Retry decorator with exponential backoff.

    Args:
        exceptions: tuple of exception types to catch
        retries: number of retry attempts
        delay: initial delay in seconds
        backoff: multiplier for delay after each failure
    """
    def decorator(func: Callable):
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    logger.warning(
                        f"{func.__name__} failed on attempt {attempt}/{retries}: {e}"
                    )
                    if attempt == retries:
                        raise
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator
