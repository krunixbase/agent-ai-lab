import uuid

def short_uuid() -> str:
    """Return a short, URL‑safe UUID."""
    return uuid.uuid4().hex[:12]
