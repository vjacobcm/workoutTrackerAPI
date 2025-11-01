from fastapi import FastAPI
from app.api.exercisedata import exerciseDataRouter as exerciseDataRouter
from app.api.workout import workoutRouter as workoutRouter

app = FastAPI()
app.include_router(exerciseDataRouter)
app.include_router(workoutRouter)


@app.get("/")
def root():
    return {"message": "Hello, world!"}