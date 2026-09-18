from sqlalchemy import CheckConstraint, Column, ForeignKey, Integer, String

from app.database.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    username = Column(String(12), unique=True, nullable=False, index=True)
    password = Column(String(255), nullable=False)
    role = Column(String(20), nullable=False)
    restaurant_id = Column(
        Integer,
        ForeignKey("restaurants.id"),
        nullable=True
    )

    __table_args__ = (
        CheckConstraint(
            "role IN ('admin', 'staff', 'direction')",
            name="check_user_role"
        ),
    )