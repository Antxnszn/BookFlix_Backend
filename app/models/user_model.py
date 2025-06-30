# server/app/models/user_model.py
# Este archivo contendría las clases de modelos de tu base de datos
# si estuvieras usando un ORM como SQLAlchemy.
# Por ahora, dado que estás usando Flask-MySQLdb directamente con cursores,
# este archivo puede quedar vacío o servir solo como un marcador de posición.

# from app import db # Si usaras Flask-SQLAlchemy

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     email = db.Column(db.String(100), unique=True, nullable=False)
#     password_hash = db.Column(db.String(255), nullable=False)
#     birthdate = db.Column(db.Date, nullable=False)
#     # Relación con géneros
#     genres = db.relationship('Genre', secondary='user_genres', backref='users', lazy=True)

# class Genre(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), unique=True, nullable=False)

# class UserGenre(db.Model):
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
#     genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'), primary_key=True)

