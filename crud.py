from sqlalchemy.orm import Session
from models import User
from auth import hash_password

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user_data):
    hashed_pw = hash_password(user_data.password)
    new_user = User(
        firstname=user_data.firstname,
        lastname=user_data.lastname,
        phone=user_data.phone,
        address=user_data.address,
        email=user_data.email,
        hashed_password=hashed_pw
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
