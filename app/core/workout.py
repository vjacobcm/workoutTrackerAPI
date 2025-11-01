from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime
from typing import List, Optional
from .exercise import Exercise
from uuid import UUID, uuid4


class Workout(BaseModel):
    user : str
    workoutId : UUID = Field(default_factory=uuid4)
    description : Optional[str] = None
    startTime : datetime = Field(default_factory=datetime.now)
    endTime : datetime = None
    exercises : List[Exercise] = None