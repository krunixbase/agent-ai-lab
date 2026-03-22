def ensure_not_empty(value: str, name: str = "value"):
    if not value or not value.strip():
        raise ValueError(f"{name} cannot be empty")
    return value
