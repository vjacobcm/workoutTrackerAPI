from pydantic import BaseModel, Field
from enum import Enum
from app.core.exerciseset import ExerciseSet
from app.core.exercisedata import ExerciseData
from uuid import UUID, uuid4
from typing import List

class Exercise(BaseModel):
    exerciseData: ExerciseData
    comments : str
    workoutId : UUID
    exerciseId : UUID = Field(default_factory=uuid4)
    sets: List[ExerciseSet]
