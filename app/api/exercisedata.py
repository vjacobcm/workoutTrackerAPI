from fastapi import APIRouter
from app.core.exercisedata import ExerciseData, TargetMuscleGroup, MuscleGroupTag, Equipment

exerciseDataRouter = APIRouter()

# exercise1 = ExerciseData(
#     name="Bench Press",
#     description="Lie on a bench and push the barbell up and down over your chest.",
#     tags=[
#         TargetMuscleGroup(name="Chest", muscleGroupTag=MuscleGroupTag.primary),
#         TargetMuscleGroup(name="Triceps", muscleGroupTag=MuscleGroupTag.secondary),
#         TargetMuscleGroup(name="Shoulders", muscleGroupTag=MuscleGroupTag.secondary)
#     ],
#     equipment=Equipment.bb
# )

# exercise2 = ExerciseData(
#     name="Dumbbell Bicep Curl",
#     description="Curl dumbbells upward to strengthen your biceps.",
#     tags=[
#         TargetMuscleGroup(name="Biceps", muscleGroupTag=MuscleGroupTag.primary),
#         TargetMuscleGroup(name="Forearms", muscleGroupTag=MuscleGroupTag.secondary)
#     ],
#     equipment=Equipment.db
# )

# exercise3 = ExerciseData(
#     name="Cable Tricep Pushdown",
#     description="Push the cable down to target your triceps.",
#     tags=[
#         TargetMuscleGroup(name="Triceps", muscleGroupTag=MuscleGroupTag.primary),
#         TargetMuscleGroup(name="Shoulders", muscleGroupTag=MuscleGroupTag.secondary)
#     ],
#     equipment=Equipment.c
# )

# exercise4 = ExerciseData(
#     name="Leg Press",
#     description="Push the weight on the leg press machine with your legs.",
#     tags=[
#         TargetMuscleGroup(name="Quadriceps", muscleGroupTag=MuscleGroupTag.primary),
#         TargetMuscleGroup(name="Glutes", muscleGroupTag=MuscleGroupTag.secondary),
#         TargetMuscleGroup(name="Hamstrings", muscleGroupTag=MuscleGroupTag.secondary)
#     ],
#     equipment=Equipment.m
# )


# exercises = [exercise1,exercise2,exercise3,exercise4]
exercises = []

@exerciseDataRouter.get("/exercises/")
async def getExercises():
    return exercises

@exerciseDataRouter.post("/exercises/")
async def addExercise(exercise: ExerciseData):
    exercises.append(exercise)
    return exercises