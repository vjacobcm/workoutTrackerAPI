from pydantic import BaseModel
from enum import Enum
from uuid import UUID


class SetType(str, Enum):
    wu = "warm-up"
    w = "working"
    d = "drop set"

class ExerciseSet(BaseModel):
    exerciseId : UUID
    setNo : int
    setType : SetType
    repetitions : int
    weight : int