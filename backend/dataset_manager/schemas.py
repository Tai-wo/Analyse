from pydantic import BaseModel


class DatasetResponse(BaseModel):

    id: int

    name: str

    file_path: str

    rows: int

    columns: int

    class Config:

        from_attributes = True
        