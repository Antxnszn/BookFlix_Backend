# server/app/config.py
import os
from dotenv import load_dotenv

load_dotenv()  # Carga las variables del archivo .env

class Config:
    MYSQL_HOST = os.getenv("MYSQL_HOST")
    MYSQL_USER = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
    MYSQL_DB = os.getenv("MYSQL_DB")
    SECRET_KEY = os.getenv("SECRET_KEY")
