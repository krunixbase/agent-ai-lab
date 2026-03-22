import json

def pretty_json(data) -> str:
    """Return pretty‑printed JSON string."""
    return json.dumps(data, indent=2, ensure_ascii=False)

def truncate(text: str, max_len: int = 200) -> str:
    """Truncate long text with ellipsis."""
    return text if len(text) <= max_len else text[:max_len] + "..."
