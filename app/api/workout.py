from fastapi import APIRouter
from app.core.workout import Workout

workoutRouter = APIRouter()

workouts = []

@workoutRouter.get("/workouts/")
async def getWorkouts():
    return workouts

@workoutRouter.post("/workouts/")
async def newWorkout(workout: Workout):
    workouts.append(workout)
    return workout.workoutId