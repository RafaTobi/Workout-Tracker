from typing import List

from psycopg2 import sql

from app.db.connection import get_connection
from app.models.exercise import WorkoutExerciseIn


def add_workout_plan_exercise(plan_id: int, exercises: List[WorkoutExerciseIn]):
    insert_query = sql.SQL(
        """
        INSERT INTO workout_plan_exercise (set_nr, reps, weight, exercise_id, workout_plan_id)
        VALUES (%s, %s, %s, %s, %s);
        """
    )
    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                values = []
                for exercise in exercises:
                    ex_id = exercise.exercise_id
                    for s in exercise.sets:
                        values.append([s.set_nr, s.reps, s.weight, ex_id, plan_id])

                cursor.executemany(
                    insert_query,
                    values
                )
    except Exception as e:
        print("A database error has occured: ", e)
    pass


def delete_workout_plan_exercise_db(wpe_id: int):
    # Query to delete all workout_plan_exercises associated with current workout_plan
    delete_query = sql.SQL(
        """
        DELETE FROM workout_plan_exercise WHERE workout_plan_id = %s
        """
    )

    try:
        with get_connection() as conn:
            with conn.cursor() as cursor:
                # Delete WPE
                cursor.execute(delete_query, (wpe_id,))
    except Exception as e:
        print("A database error has occurred: ", e)
