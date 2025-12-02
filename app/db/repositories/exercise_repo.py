from app.db.connection import get_connection


def get_all_exercises():
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT * FROM exercise;
                    """
                )
                return cur.fetchall()
    except Exception as e:
        print("A database error has occurred: ", e)


def insert_exercise(name, desc, cat):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO exercise (name, description, category)
                    VALUES (%s, %s, %s);
                    """,
                    (name, desc, cat)
                )
    except Exception as e:
        print("A database error has occurred: ", e)
