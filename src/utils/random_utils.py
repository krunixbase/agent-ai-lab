import random
import string

def random_token(length: int = 16) -> str:
    """Generate a random alphanumeric token."""
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(length))

def choose_one(items):
    """Return a random element from a list."""
    if not items:
        raise ValueError("Cannot choose from an empty list")
    return random.choice(items)
