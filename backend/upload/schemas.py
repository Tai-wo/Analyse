from pydantic import BaseModel


class UploadResponse(BaseModel):

    dataset_id: int

    filename: str

    rows: int

    columns: int

    message: str