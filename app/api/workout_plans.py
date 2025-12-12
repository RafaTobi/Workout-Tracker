from fastapi import APIRouter
from app.db.repositories.workout_plan_repo import *
from app.models.workout_plan import WorkoutExerciseIn, WorkoutPlanUpdate

router = APIRouter(tags=["Workout Plans"])


@router.get('/workout-plans/all')
async def get_all():
    return fetch_all_workout_plans()


@router.get('/workout-plans/{id}')
async def get_by_id(id: int):
    return fetch_workout_plan_by_id(id)


@router.post('/workout-plans/new')
async def create_workout_plan(workoutplan: WorkoutPlanBase):
    add_workout_plan(wp_ex=workoutplan)


@router.put('/workout-plans/update/{id}')
async def update_workout_plan(id: int, workoutplan_update: WorkoutPlanUpdate):
    update_workout_plan_db(workoutplan_update)