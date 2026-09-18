from fastapi import FastAPI

from app.database.database import Base, engine
from app.database import models
from app.database.seed import seed_admin
from app.routers.auth import router as auth_router


Base.metadata.create_all(bind=engine)

seed_admin()


app = FastAPI(
    title="Ytasty Crousty API",
    description="API backend pour Ytasty Crousty",
    version="1.0.0",
)


app.include_router(auth_router)


@app.get("/")
def accueil():
    return {
        "message": "Bienvenue sur l'API Ytasty Crousty"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }