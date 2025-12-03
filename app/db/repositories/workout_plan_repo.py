from app.db.connection import get_connection


def create_workout_plan(name, description, schedule):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO workout_plan (name, description, schedule)
                    VALUES (%s, %s, %s);
                    """,
                    (name, description, schedule)
                )
    except Exception as e:
        print("A database error has occurred: ", e)


def get_all_workout_plans():
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT * FROM workout_plan;
                    """
                )
                return cur.fetchall()
    except Exception as e:
        print("A database error has occurred: ", e)
