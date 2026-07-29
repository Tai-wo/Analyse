from pydantic import BaseModel
from typing import Dict


class WorkspaceResponse(BaseModel):

    dataset_id: int

    dataset_name: str

    rows: int

    columns: int

    modules: Dict[str, bool]