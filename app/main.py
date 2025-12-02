from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import exercises


app = FastAPI()
app.include_router(exercises.router)


origins = [""]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"Detail": "This is a Workout Tracker API"}
