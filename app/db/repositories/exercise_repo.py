from app.db.connection import get_connection
from app.models.exercise import *


def create_exercise(exercise: ExerciseBase): # FIXME basemodel?
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO exercise (name, description, category)
                    VALUES (%s, %s, %s);
                    """,
                    (exercise.name, exercise.description, exercise.category)
                )
    except Exception as e:
        print("A database error has occurred: ", e)


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

def get_exercise_by_id(id: int):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT * FROM exercise
                    WHERE id=%s;
                    """,
                    (id,)
                )
                return cur.fetchone()
    except Exception as e:
        print("A database error has occurred: ", e)
