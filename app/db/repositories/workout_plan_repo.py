from psycopg2 import sql

from app.db.connection import get_connection
from app.db.repositories.workout_plan_exercise_repo import add_workout_plan_exercise, delete_workout_plan_exercise_db
from app.models.workout_plan import WorkoutPlanUpdate, WorkoutPlanBase


def add_workout_plan(wp_ex: WorkoutPlanBase):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO workout_plan (name, description)
                    VALUES (%s, %s)
                    RETURNING id;
                    """,
                    (wp_ex.name, wp_ex.description)
                )
                wp_id = cur.fetchone()[0]
                conn.commit()

                add_workout_plan_exercise(wp_id, wp_ex.exercises)
    except Exception as e:
        print("A database error has occurred: ", e)


def fetch_all_workout_plans():
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


def fetch_workout_plan_by_id(wp_id: int):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT * FROM workout_plan
                    WHERE id = %s;
                    """,
                    (wp_id,)
                )
                return cur.fetchone()
    except Exception as e:
        print("A database error has occurred: ", e)


def update_workout_plan_db(wp_up: WorkoutPlanUpdate):
    # Query to update current workout_plan values
    update_query = sql.SQL(
        """
        UPDATE workout_plan
        SET name = %s, description = %s
        WHERE id = %s
        """
    )

    wp_id = wp_up.plan_id
    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                # Update WP
                cursor.execute(
                    update_query,
                    (
                        wp_up.name, wp_up.description, wp_id
                    ))

                # Delete old WPE
                delete_workout_plan_exercise_db(wp_id)
                # Add new WPE
                add_workout_plan_exercise(wp_id, wp_up.exercises)
    except Exception as e:
        print("A database error has occurred: ", e)


def delete_workout_plan_db(wp_id: int):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    DELETE FROM workout_plan
                    WHERE id = %s;
                    """,
                    (wp_id,)
                )
                return cur.fetchone()
    except Exception as e:
        print("A database error has occurred: ", e)
