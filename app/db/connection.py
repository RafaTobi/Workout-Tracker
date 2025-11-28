import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()

USER = os.getenv("DATABASE_USER")
PASSWORD = os.getenv("DATABASE_PASSWD")
DATABASE = os.getenv("DATABASE_NAME")

CREATE_TABLES = [
    """
    CREATE TABLE IF NOT EXISTS exercise (
    id          INTEGER PRIMARY KEY,
    name        VARCHAR(50) NOT NULL,
    description TEXT,
    category    VARCHAR(50) NOT NULL
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS workout_plan (
    id          INTEGER PRIMARY KEY,
    name        VARCHAR (50) NOT NULL,
    description TEXT,
    schedule    TIMESTAMP
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS workout_plan_exercise (
    id              INTEGER PRIMARY KEY,
    reps            INTEGER NOT NULL,
    weight          NUMERIC(6,2) NOT NULL,
    exercise_id     INTEGER REFERENCES exercise(id) ON DELETE CASCADE,
    workout_plan_id INTEGER REFERENCES workout_plan(id) ON DELETE CASCADE
    );
    """
]

try:
    with psycopg2.connect(
            database=DATABASE,
            user=USER,
            password=PASSWORD,
            host="localhost",
            port="54326"
    ) as conn:
        with conn.cursor() as cur:
            for table in CREATE_TABLES:
                cur.execute(table)
except Exception as e:
    print("An error has occurred: ", e)
