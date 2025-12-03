from fastapi import APIRouter
from app.db.repositories.workout_plan_repo import *


router = APIRouter(tags=["Workout Plans"])


@router.get('/workout-plans/all')
async def get_all():
    return get_all_workout_plans()
