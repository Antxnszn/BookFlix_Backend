# server/app/utils/password_hash.py
from bcrypt import hashpw, gensalt, checkpw

def hash_password(password: str) -> str:
    """
    Hashea una contraseña usando bcrypt.
    """
    # gensalt() genera un salt aleatorio cada vez
    # hashpw toma la contraseña (bytes) y el salt (bytes)
    hashed = hashpw(password.encode('utf-8'), gensalt())
    return hashed.decode('utf-8') # Decodifica a string para guardar en la DB

def check_password(password: str, hashed_password: str) -> bool:
    """
    Verifica si una contraseña coincide con su hash.
    """
    # checkpw toma la contraseña (bytes) y el hash (bytes)
    return checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
