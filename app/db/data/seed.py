from app.db.connection import get_connection


with get_connection() as conn:
    with conn.cursor() as cur:
        print("Connection: ", conn)
        print("Cursor    : ", cur)
