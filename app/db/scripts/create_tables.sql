CREATE TABLE IF NOT EXISTS exercise (
    id          SERIAL PRIMARY KEY,
    name        VARCHAR (50) NOT NULL,
    description TEXT,
    category    VARCHAR (50) NOT NULL
);

CREATE TABLE IF NOT EXISTS workout_plan (
    id          SERIAL PRIMARY KEY,
    name        VARCHAR (50) NOT NULL,
    description TEXT,
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS workout_plan_exercise (
    id              SERIAL PRIMARY KEY,
    set_nr          INTEGER NOT NULL,
    reps            INTEGER NOT NULL,
    weight          NUMERIC (6,2) NOT NULL,
    exercise_id     INTEGER REFERENCES exercise(id) ON DELETE CASCADE,
    workout_plan_id INTEGER REFERENCES workout_plan(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS scheduled_workout (
    id              SERIAL PRIMARY KEY,
    scheduled_date  DATE,
    scheduled_time  TIME,
    status          VARCHAR (10),
    workout_plan_id INTEGER REFERENCES workout_plan(id) ON DELETE CASCADE
)