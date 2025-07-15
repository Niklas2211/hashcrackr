import hashlib


def get_hash_function(algorithm):
    try:
        return getattr(hashlib, algorithm)
    except AttributeError:
        return None


def detect_hash_type(hash_string):
    length = len(hash_string)

    if length == 32:
        return "md5"
    elif length == 40:
        return "sha1"
    elif length == 64:
        return "sha256"
    elif length == 128:
        return "sha512"
    elif hash_string.startswith("$2a$") or hash_string.startswith("$2b$"):
        return "bcrypt"

    return "unknown"
