from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class MessageHash(Base):
    __tablename__ = "MessageHash"

    id = Column(Integer, primary_key=True, index=True)
    message = Column(String, unique=True, index=True)
    hash = Column(String, index=True)
