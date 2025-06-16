from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schema.user_schema import ForgotPassword
import crud
from database import get_db

router = APIRouter()

@router.post("/forgot-password")
def forgot_password(request: ForgotPassword, db: Session = Depends(get_db)):
    user = crud.get_user_by_email(db, request.email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return {"message": f"Password reset link sent to {request.email}"}
