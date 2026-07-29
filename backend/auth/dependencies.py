from fastapi import Depends
from sqlalchemy.orm import Session

from database.db import SessionLocal
from auth.models import User


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


def get_current_user(
    db: Session = Depends(get_db)
):

    user = db.query(User).first()

    return user