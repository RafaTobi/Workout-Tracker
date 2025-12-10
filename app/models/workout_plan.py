from datetime import datetime
from typing import List

from pydantic import BaseModel

from app.models.exercise import WorkoutExerciseIn


class WorkoutPlanExerciseIn(BaseModel):
    name: str
    description: str
    exercises: List[WorkoutExerciseIn]
