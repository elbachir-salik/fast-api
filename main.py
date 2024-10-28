from fastapi import FastAPI
from models import User, Gender, Role
from typing import List
from uuid import uuid4

app = FastAPI()

db: List[User] = [
    
    User(id=uuid4(), fist_name="elbachir", last_name="salik", gender=Gender.male, roles=[Role.student]),
    User(id=uuid4(), fist_name="queen", last_name="morgan", gender=Gender.female, roles=[Role.admin,Role.user])
]


@app.get("/")
def read_root():
    return {"Hello": "Salik"}