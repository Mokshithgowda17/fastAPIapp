from pydantic import BaseModel
from typing import Optional

class JobCreate(BaseModel):
    name:str
    location:str

class JobUpdate(BaseModel):
    name:Optional[str]=None
    location: Optional[str]=None