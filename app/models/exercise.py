from typing import List

from pydantic import BaseModel


class ExerciseBase(BaseModel):
    name: str
    description: str
    category: str


class Set(BaseModel):
    set_nr: int
    reps: int
    weight: float


class WorkoutExerciseIn(BaseModel):
    exercise_id: int
    sets: List[Set]
