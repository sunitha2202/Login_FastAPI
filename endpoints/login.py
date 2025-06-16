from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from auth import verify_password, create_access_token
from schema.user_schema import LoginRequest, Token
import crud
from database import get_db

router = APIRouter()

@router.post("/login")
def login(request: LoginRequest, db: Session = Depends(get_db)):
    user = crud.get_user_by_email(db, request.email)
    if not user or not verify_password(request.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    token = create_access_token(data={"sub": user.email})
    return {"access_token": token, "token_type": "bearer","message":"loggedin successfully"}

