from fastapi import APIRouter, HTTPException
from app.schemas.user import UserCreate, UserResponse

router = APIRouter()

@router.post("/register")
def register():
    pass

@router.post("/login")
def login():
    pass
