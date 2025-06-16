from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "postgresql://postgres:mobsys@localhost:5432/myfirstapidb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

try:
    with engine.connect() as connection:
        print("✅ Database connected successfully!")
except Exception as e:
    print("❌ Failed to connect to the database:")
    print(e)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()