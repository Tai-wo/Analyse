from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from database.db import SessionLocal

from dataset_manager.services import (
    get_all_datasets,
    get_dataset_by_id,
    delete_dataset
)

router = APIRouter(

    prefix="/datasets",

    tags=["Datasets"]

)


def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()


@router.get("/")
def list_datasets(

    db: Session = Depends(get_db)

):

    return get_all_datasets(
        db
    )


@router.get("/{dataset_id}")
def get_dataset(

    dataset_id: int,

    db: Session = Depends(get_db)

):

    return get_dataset_by_id(

        db,

        dataset_id

    )


@router.delete("/{dataset_id}")
def remove_dataset(

    dataset_id: int,

    db: Session = Depends(get_db)

):

    return delete_dataset(

        db,

        dataset_id

    )