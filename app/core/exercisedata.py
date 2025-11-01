from pydantic import BaseModel, Field
from enum import Enum
from typing import List
from uuid import UUID, uuid4

class Equipment(str, Enum):
    db = "dumbbell"
    bb = "barbell"
    m = "machine"
    s = "smith machine"
    c = "cable"

class MuscleGroupTag(str, Enum):
    primary = "primary"
    secondary = "secondary"

class TargetMuscleGroup(BaseModel):
    name: str
    muscleGroupTag: MuscleGroupTag 

class ExerciseData(BaseModel):
    id : UUID = Field(default_factory=uuid4)
    name: str
    description: str
    tags: List[TargetMuscleGroup]
    equipment : Equipment
