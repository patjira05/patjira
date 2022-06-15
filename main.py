import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class User(BaseModel):
    ID : Optional[int]
    username : Optional[str]
    password : Optional[str]

@app.get("/")
async def read_root():
    return {"Con": "Start"}


@app.get("/my_name")
async def my_name():
    data = "Nontakorn Konakin"
    return data


@app.get("/input_name")
async def input_name(name):
    data = name
    return data

@app.get("/area_square")
async def area_square(width, hight):
    area = float(width) * float(hight)
    data = "area square : {}".format(area)
    return data

@app.get("/area_triangle")
async def area_triangle(base,hight):
    area = 0.5*float(base)*float(hight)
    data ="area triangle: {}".format(area)
    return data

@app.get("/cf_and_ca")
async def circle (radius):
    c = 2*3.14* float(radius)
    r = 3.14*float(radius)*float(radius)
    obj = {"c": c, "area":r}
    data = []
    error = {"error" : False}
    data.append(obj)
    data.append(error)
    return data


@app.post("/test_post")
async def test_post():
    return {"test": "post"}


@app.post("/login")
async def login(user :User):
    uUser = 'test'
    uPassword = '12345'
    if(user.username == uUser and user.password == uPassword):
        data = {"login" : "Succeses","error":False}
    else:
        data = {"login" : "Fail","error":True}
    return data

if __name__ == "__main__":
    uvicorn.run(app, host="192.168.1.2", port=8000)