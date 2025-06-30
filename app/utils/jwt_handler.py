# server/app/utils/jwt_handler.py
import jwt
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv() # Cargar variables de entorno

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = "HS256" # Algoritmo de hash para JWT

def generate_token(user_id: int, email: str, name: str, genres: list = None) -> str:
    """
    Genera un token JWT para un usuario.
    Incluye ID de usuario, email, nombre y géneros en el payload.
    El token expira en 24 horas.
    """
    if genres is None:
        genres = []

    payload = {
        "user_id": user_id,
        "email": email,
        "name": name,
        "genres": genres, # Incluye los géneros favoritos del usuario
        "exp": datetime.utcnow() + timedelta(days=1), # Token expira en 24 horas
        "iat": datetime.utcnow() # Issued at (momento de emisión)
    }
    # Codifica el payload usando la SECRET_KEY y el algoritmo especificado
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

def decode_token(token: str):
    """
    Decodifica un token JWT y retorna su payload.
    Maneja errores si el token es inválido o ha expirado.
    """
    try:
        # Decodifica el token usando la SECRET_KEY y el algoritmo
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        return {"error": "Token ha expirado"}
    except jwt.InvalidTokenError:
        return {"error": "Token inválido"}

