from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.database.database import SessionLocal
from app.database.models.user import User


def seed_admin():
    db: Session = SessionLocal()

    try:
        existing_admin = db.query(User).filter(
            User.username == "admin123"
        ).first()

        if existing_admin:
            return

        admin = User(
            first_name="Admin",
            last_name="Ytasty",
            username="admin123",
            hashed_password=hash_password("Admin@123456"),
            role="admin",
            restaurant_id=None
        )

        db.add(admin)
        db.commit()

    finally:
        db.close()