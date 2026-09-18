from sqlalchemy import Boolean, Column, Integer, String, Text

from app.database.database import Base


class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    city = Column(String(100), nullable=False)
    address = Column(String(255), nullable=False)
    is_open = Column(Boolean, nullable=False, default=True)
    opening_hours = Column(Text, nullable=False)
    contact = Column(String(255), nullable=False)