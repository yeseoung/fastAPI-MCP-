from fastapi import APIRouter, Body, HTTPException
from pydantic import BaseModel
from AUTH.token import create_access_token #토큰 부여
from repositories.Student_repo import *

router = APIRouter(prefix="/auth", tags=["auth"])

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(req: LoginRequest):
    username = req.username
    password = req.password
    t = get_student_by_name(username)
    if username != t["name"] or password != str(t["student_id"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_access_token({"sub": username})
    return {"access_token": token, "token_type": "bearer"}