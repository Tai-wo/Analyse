from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey

from database.db import Base


class Workspace(Base):

    __tablename__ = "workspaces"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    dataset_id = Column(
        Integer,
        ForeignKey("datasets.id")
    )