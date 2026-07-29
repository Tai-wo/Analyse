from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from database.db import Base


class Dataset(Base):

    __tablename__ = "datasets"

    id = Column(
        Integer,
        primary_key=True
    )

    name = Column(
        String
    )

    file_path = Column(
        String
    )