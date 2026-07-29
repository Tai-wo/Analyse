from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from database.db import SessionLocal

from dataset_manager.services import (
    get_dataset
)

router = APIRouter(
    prefix="/profile",
    tags=["Profiling"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.get("/{dataset_id}")
def profile_dataset(

    dataset_id: int,

    db: Session = Depends(get_db)

):

    dataset = get_dataset(
        db,
        dataset_id
    )

    if not dataset:

        return {
            "error": "Dataset not found"
        }

    return {

        "dataset_id": dataset.id,

        "rows": dataset.rows,

        "columns": dataset.columns

    }