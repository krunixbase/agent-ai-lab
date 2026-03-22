import os

def get_env(name: str, default=None):
    """Return environment variable or default if missing."""
    return os.getenv(name, default)

def require_env(name: str) -> str:
    """Return environment variable or raise error if missing."""
    value = os.getenv(name)
    if value is None:
        raise EnvironmentError(f"Missing required environment variable: {name}")
    return value
