from app.db.connection import get_connection
from app.models.workout_plan import WorkoutPlanExerciseIn


def create_workout_plan_with_exercises(wp_ex: WorkoutPlanExerciseIn):
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

                values = []
                for exercise in wp_ex.exercises:
                    ex_id = exercise.exercise_id
                    for s in exercise.sets:
                        values.append([s.set_nr, s.reps, s.weight, ex_id, wp_id])

                cur.executemany(
                    """
                    INSERT INTO workout_plan_exercise (set_nr, reps, weight, exercise_id, workout_plan_id)
                    VALUES (%s, %s, %s, %s, %s);
                    """,
                    values
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


def get_workout_plan_by_id(id: int):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT * FROM workout_plan
                    WHERE id=%s;
                    """,
                    (id,)
                )
                return cur.fetchone()
    except Exception as e:
        print("A database error has occurred: ", e)
