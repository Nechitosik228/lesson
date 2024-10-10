from . import UserInput,UserOutput,app



@app.post("/user")
def create(data:UserInput):
    name = data.name
    job = data.job
    return UserOutput(name=name,job=job)




