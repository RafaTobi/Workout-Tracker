from datetime import datetime
from typing import List

from pydantic import BaseModel

from app.models.exercise import WorkoutExerciseIn


class WorkoutPlanBase(BaseModel):
    name: str
    description: str
    exercises: List[WorkoutExerciseIn]


class WorkoutPlanUpdate(WorkoutPlanBase):
    plan_id: int
