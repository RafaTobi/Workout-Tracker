import psycopg2
from app.core.config import settings


USER = settings.DB_USER
PASSWORD = settings.DB_PASS
DATABASE = settings.DB_NAME
HOST = settings.DB_HOST
PORT = settings.DB_PORT

def get_connection():
    return psycopg2.connect(
        database=DATABASE,
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT
    )
