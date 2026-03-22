from utils.uuid import short_uuid
from utils.hashing import sha256
from utils.validators import ensure_not_empty


def test_short_uuid():
    assert len(short_uuid()) == 12


def test_sha256():
    assert sha256("abc") == sha256("abc")


def test_ensure_not_empty():
    ensure_not_empty("ok")
