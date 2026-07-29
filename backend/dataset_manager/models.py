from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from database.db import Base


class Dataset(Base):

    __tablename__ = "datasets"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String,
        nullable=False
    )

    file_path = Column(
        String,
        nullable=False
    )

    rows = Column(
        Integer,
        default=0
    )

    columns = Column(
        Integer,
        default=0
    )

    owner_id = Column(
        Integer,
        ForeignKey("users.id")
    )