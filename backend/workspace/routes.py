from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from database.db import SessionLocal

from dataset_manager.models import Dataset

from workspace.services import (
    build_workspace_data
)

router = APIRouter(
    prefix="/workspace",
    tags=["Workspace"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.get("/{dataset_id}")
def get_workspace(
    dataset_id: int,
    db: Session = Depends(get_db)
):

    dataset = db.query(
        Dataset
    ).filter(
        Dataset.id == dataset_id
    ).first()

    if not dataset:

        return {
            "error": "Dataset not found"
        }

    return build_workspace_data(
        dataset
    )