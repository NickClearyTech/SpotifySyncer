from cryptography.fernet import Fernet
from settings import ENCRYPTION_KEY


def encrypt(message: str) -> bytes:
    f = Fernet(ENCRYPTION_KEY.encode("utf-8"))
    return f.encrypt(message.encode("utf-8"))


def decrypt(message: bytes) -> str:
    f = Fernet(ENCRYPTION_KEY.encode("utf-8"))
    return f.decrypt(message).decode("utf-8")
