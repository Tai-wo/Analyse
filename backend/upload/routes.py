from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import Depends

from sqlalchemy.orm import Session

from database.db import SessionLocal

from upload.services import (
    save_file,
    create_dataset_record
)

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post("/")
def upload_file(

    file: UploadFile = File(...),

    db: Session = Depends(get_db)

):

    file_path = save_file(
        file
    )

    dataset = create_dataset_record(

        db,

        file.filename,

        file_path
    )

    return {

        "dataset_id": dataset.id,

        "filename": dataset.name,

        "rows": dataset.rows,

        "columns": dataset.columns,

        "message": "Upload successful"

    }