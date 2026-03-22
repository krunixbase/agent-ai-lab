import hashlib

def sha256(text: str) -> str:
    """Return SHA256 hash of a string."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def md5(text: str) -> str:
    """Return MD5 hash of a string (non-cryptographic)."""
    return hashlib.md5(text.encode("utf-8")).hexdigest()
