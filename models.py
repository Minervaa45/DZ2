from sqlalchemy import Column, DateTime, Integer, String, func

from db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    email = Column(String(320), nullable=False, unique=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
