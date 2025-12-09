import uvicorn
from app.db.data.seed import seed_exercise_data

if __name__ == '__main__':
    seed_exercise_data()
    uvicorn.run('app.main:app', host='127.0.0.1', port=8000, reload=True)