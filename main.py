from fastapi import FastAPI, HTTPException
from models import User, Gender, Role, UserUpdateModel
from typing import List
from uuid import UUID

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
            return
    raise HTTPException(
        status_code=404,
        detail= f"User with id : {user_id} not found"
    )


@app.put("/api/users")
async def update_user(user_update: UserUpdateModel, user_id: UUID):
    for user in db:
        if user_id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id : {user_id} not found"
    )
