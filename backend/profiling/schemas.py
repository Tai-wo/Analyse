from pydantic import BaseModel
from typing import Dict


class ProfileResponse(BaseModel):

    dataset_id: int

    rows: int

    columns: int

    duplicate_rows: int

    missing_values: int

    column_types: Dict[str, str]