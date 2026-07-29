from pydantic import BaseModel


class PythonExportResponse(BaseModel):

    dataset_id: int

    code: str


class FileExportResponse(BaseModel):

    dataset_id: int

    message: str

    file_path: str