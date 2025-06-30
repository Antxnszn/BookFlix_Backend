from flask import Blueprint, request, jsonify
from app import mysql

favorite_bp = Blueprint("favorites", __name__, url_prefix="/api/favorites")

@favorite_bp.route("/", methods=["POST"])
def add_favorite():
    data = request.get_json()
    user_id = data["userId"]
    book_id = data["bookId"]

    cursor = mysql.connection.cursor()
    try:
        cursor.execute(
            "INSERT IGNORE INTO user_favorites (user_id, book_id) VALUES (%s, %s)",
            (user_id, book_id)
        )
        mysql.connection.commit()
        return jsonify({"success": True}), 200
    except Exception as e:
        mysql.connection.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()


@favorite_bp.route("/<int:user_id>", methods=["GET"])
def get_favorites(user_id):
    cursor = mysql.connection.cursor()
    try:
        cursor.execute(
            "SELECT book_id FROM user_favorites WHERE user_id = %s", (user_id,)
        )
        rows = cursor.fetchall()
        book_ids = [row[0] for row in rows]
        return jsonify({"favoriteIds": book_ids}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
