from pydantic import BaseModel



class UserInput(BaseModel):
    name:str
    job:str|None
    age:int
    wealth:float



class UserOutput(BaseModel):
    name:str
    job:str|None