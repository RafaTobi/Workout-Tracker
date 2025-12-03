from fastapi import APIRouter
from app.db.repositories.exercise_repo import *


router = APIRouter(tags=["Exercises"])

@router.get('/exercise/all')
async def get_all():
    return get_all_exercises()


@router.get('/exercise/{id}')
async def get_exercise(id: int):
    return get_exercise_by_id(id)
