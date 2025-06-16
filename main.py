from fastapi import FastAPI
from model.user_model import Base
from database import engine
from endpoints import register, login, forgot_password

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(register.router)
app.include_router(login.router)
app.include_router(forgot_password.router)
