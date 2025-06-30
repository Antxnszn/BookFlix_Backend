# server/app/routes/auth_routes.py
from flask import Blueprint, request, jsonify
# Importar mysql desde el archivo de inicialización de la app

from app import mysql
from app.utils.password_hash import hash_password, check_password 
from app.utils.jwt_handler import generate_token

user_bp = Blueprint("auth", __name__, url_prefix="/api/auth")



@user_bp.route("/", methods=["GET"])
# def auth_root():
#     return jsonify({"message": "Auth funciona correctamente"}), 200

@user_bp.route("/register", methods=["POST", "GET"])
def register():
    if request.method == 'POST':
        data = request.get_json()
        name = data.get("name")
        email = data.get("email")
        birthdate = data.get("birthdate")
        password = data.get("password")
        favorite_genres = data.get("genres", [])  # Lista de nombres de géneros

        # Validación básica de entrada
        if not all([name, email, birthdate, password]):
            return jsonify({"error": "Todos los campos obligatorios son requeridos"}), 400
        if not isinstance(favorite_genres, list):
            return jsonify({"error": "Los géneros deben ser una lista"}), 400
        if len(password) < 6:
            return jsonify({"error": "La contraseña debe tener al menos 6 caracteres"}), 400

        hashed_pw = hash_password(password)

        try:
            cursor = mysql.connection.cursor()

            # Verificar si ya existe el correo
            cursor.execute("SELECT id FROM users WHERE email = %s", (email,))
            existing_user = cursor.fetchone()
            if existing_user:
                cursor.close()
                return jsonify({"error": "El correo electrónico ya está registrado"}), 409

            # Insertar usuario
            cursor.execute(
                "INSERT INTO users (name, birthdate, email, password_hash) VALUES (%s, %s, %s, %s)",
                (name, birthdate, email, hashed_pw)
            )
            mysql.connection.commit()
            user_id = cursor.lastrowid

            # Insertar géneros y relaciones
            for genre_name in favorite_genres:
                cursor.execute("SELECT id FROM genres WHERE name = %s", (genre_name,))
                genre_row = cursor.fetchone()
                genre_id = genre_row[0] if genre_row else None

                if not genre_id:
                    cursor.execute("INSERT INTO genres (name) VALUES (%s)", (genre_name,))
                    mysql.connection.commit()
                    genre_id = cursor.lastrowid

                cursor.execute(
                    "INSERT INTO user_genres (user_id, genre_id) VALUES (%s, %s)",
                    (user_id, genre_id)
                )
                mysql.connection.commit()

            cursor.close()

            token = generate_token(user_id, email, name, favorite_genres)
            return jsonify({
                "message": "Usuario registrado exitosamente",
                "token": token,
                "user_name": name,
                "user_id": user_id,
                "genres": favorite_genres 
            }), 201

        except Exception as e:
            mysql.connection.rollback()
            print(f"Error en el registro: {e}")
            return jsonify({"error": "Error interno del servidor al registrar el usuario"}), 500

    # Si no es POST
    return jsonify({"message": "Usa POST para registrar usuarios"}), 405

@user_bp.route("/login", methods=["POST"])
def login():
    """
    Ruta para iniciar sesión de un usuario.
    Recibe el email y la contraseña.
    Verifica las credenciales y, si son correctas, retorna un token JWT.
    """
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if not all([email, password]):
        return jsonify({"error": "Email y contraseña son requeridos"}), 400

    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT id, name, password_hash FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
        cursor.close()

        if user and check_password(password, user[2]): # user[2] es password_hash
            user_id = user[0]
            user_name = user[1]

            # Obtener los géneros favoritos del usuario para incluirlos en el token
            cursor = mysql.connection.cursor()
            cursor.execute("""
                SELECT g.name FROM genres g
                JOIN user_genres ug ON g.id = ug.genre_id
                WHERE ug.user_id = %s
            """, (user_id,))
            user_genres = [row[0] for row in cursor.fetchall()]
            cursor.close()

            token = generate_token(user_id, email, user_name, user_genres)
            
            return jsonify({"message": "Inicio de sesión exitoso", "token": token, "user_name": user_name, "user_id": user_id,"genres": user_genres}), 200
        else:
            return jsonify({"error": "Credenciales inválidas"}), 401

    except Exception as e:
        print(f"Error en el login: {e}")
        return jsonify({"error": "Error interno del servidor al iniciar sesión"}), 500