from fastapi import FastAPI
from models import User, Gender, Role
from typing import List
from uuid import uuid4,UUID

app = FastAPI()

db: List[User] = [
    
    User(id=UUID("ea04b18c-93b4-417f-a9fb-d3136bf2e4c1"), fist_name="elbachir", last_name="salik", gender=Gender.male, roles=[Role.student]),
    User(id=UUID("56e7813a-bca1-43f4-9d8d-897dfb26f027"), fist_name="queen", last_name="morgan", gender=Gender.female, roles=[Role.admin,Role.user])
]


@app.get("/")
def read_root():
    return {"Hello": "Salik"}

@app.get("/api/users")
async def fetch_users():
    return db;

@app.post("/api/users")
async def add_user(user: User):
    db.append(user)
    return {"id": user.id}


@app.delete("/api/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db :
        if user_id == user_id:
            db.remove(user)