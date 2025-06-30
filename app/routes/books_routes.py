from flask import Blueprint, jsonify, request
from app.utils.jwt_handler import decode_token
import json

books_bp = Blueprint("books", __name__, url_prefix="/api/books")

@books_bp.route("/", methods=["GET"])
def get_books():
    token = request.headers.get("Authorization")
    if not token:
        return jsonify({"error": "Token requerido"}), 401

    user_data = decode_token(token.split()[1])
    genres = user_data.get("genres", [])

    with open("server/data/BookDetails.json", "r") as f:
        all_books = json.load(f)

    # Filtra los libros según géneros
    filtered = [book for book in all_books if book["genre"] in genres]

    return jsonify(filtered)
