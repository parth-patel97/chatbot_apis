from typing import Dict
from pydantic import BaseModel

class GlobalVariableSchema(BaseModel):
    name:str
    type:str
    flowId: int

    class Config:
        orm_mode = True
        underscore_attrs_are_private = True