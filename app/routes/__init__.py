# app/routes/__init__.py
from flask import Blueprint
from .auth_routes import user_bp
from .books_routes import books_bp
from .favorite_routes import favorite_bp

routes = Blueprint("routes", __name__)

routes.register_blueprint(user_bp, url_prefix="/users")
routes.register_blueprint(books_bp, url_prefix="/books")
routes.register_blueprint(favorite_bp, url_prefix="/favorites")
