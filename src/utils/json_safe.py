import json

def json_safe(data):
    """
    Safely serialize Python objects to JSON-compatible structures.
    Falls back to string representation for unsupported types.
    """
    try:
        json.dumps(data)
        return data
    except TypeError:
        return str(data)
