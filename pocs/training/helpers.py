import secrets
import string


FLAG_ALPHABET = string.ascii_uppercase + string.digits
FLAG_BODY_LENGTH = 31


def generate_flag():
    """Return a synthetic flag matching AuditFarm's default FLAG_FORMAT."""
    body = ''.join(secrets.choice(FLAG_ALPHABET) for _ in range(FLAG_BODY_LENGTH))
    return body + '='
