# server/app/__init__.py
from flask import Flask
from flask_mysqldb import MySQL # Para conectar con MySQL
from flask_cors import CORS # Para permitir solicitudes desde tu frontend React
from .config import Config # Importa la configuración


# Inicializa MySQL y CORS como variables globales (o usa un patrón de factoría de app)
mysql = MySQL()
cors = CORS()





def create_app():
    """
    Crea y configura la instancia de la aplicación Flask.
    """
    app = Flask(__name__)
    app.config.from_object(Config)  # Carga la configuración desde config.py

    # Añade prints para verificar variables cargadas
    print("MYSQL_HOST:", app.config.get("MYSQL_HOST"))
    print("MYSQL_USER:", app.config.get("MYSQL_USER"))
    print("MYSQL_PASSWORD:", app.config.get("MYSQL_PASSWORD"))
    print("MYSQL_DB:", app.config.get("MYSQL_DB"))

    # Inicializa extensiones de Flask
    mysql.init_app(app)
    cors.init_app(app, resources={r"/api/*": {"origins": "*"}})  # Permite CORS para todas las rutas /api

    # Importa y registra los Blueprints (colecciones de rutas)
    from app.routes.auth_routes import user_bp
    from app.routes.favorite_routes import favorite_bp 

    app.register_blueprint(user_bp)
    app.register_blueprint(favorite_bp)  
    # app.register_blueprint(books_bp) # Se registrará después

    @app.route('/')
    def index():
        return "Bienvenido a Bookflix API!"

    return app
