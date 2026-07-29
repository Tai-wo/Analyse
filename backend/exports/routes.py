from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from database.db import SessionLocal

from dataset_manager.models import Dataset

from exports.services import (
    export_python,
    export_excel,
    export_pdf
)

router = APIRouter(
    prefix="/exports",
    tags=["Exports"]
)


# -------------------------
# DB CONNECTION
# -------------------------
def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()


# -------------------------
# PYTHON EXPORT
# -------------------------
@router.get("/python/{dataset_id}")
def python_export(
    dataset_id: int,
    db: Session = Depends(get_db)
):

    dataset = db.query(Dataset).filter(
        Dataset.id == dataset_id
    ).first()

    if not dataset:

        return {"error": "Dataset not found"}

    return export_python(dataset)


# -------------------------
# EXCEL EXPORT
# -------------------------
@router.get("/excel/{dataset_id}")
def excel_export(
    dataset_id: int,
    db: Session = Depends(get_db)
):

    dataset = db.query(Dataset).filter(
        Dataset.id == dataset_id
    ).first()

    if not dataset:

        return {"error": "Dataset not found"}

    return export_excel(dataset)


# -------------------------
# PDF EXPORT
# -------------------------
@router.get("/pdf/{dataset_id}")
def pdf_export(
    dataset_id: int,
    db: Session = Depends(get_db)
):

    dataset = db.query(Dataset).filter(
        Dataset.id == dataset_id
    ).first()

    if not dataset:

        return {"error": "Dataset not found"}

    return export_pdf(dataset)