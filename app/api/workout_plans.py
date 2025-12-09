from fastapi import APIRouter
from app.db.repositories.workout_plan_repo import *
from app.models.workout_plan import WorkoutPlanExerciseIn

router = APIRouter(tags=["Workout Plans"])


@router.get('/workout-plans/all')
async def get_all():
    return get_all_workout_plans()


@router.get('/workout-plans/{id}')
async def get_by_id(id: int):
    return get_workout_plan_by_id(id)


@router.post('/workout-plans/new')
async def create_workout_plan(workoutplan: WorkoutPlanExerciseIn):
    create_workout_plan_with_exercises(wp_ex=workoutplan)