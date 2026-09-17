from fastapi import FastAPI

app = FastAPI(
    title="Ytasty Crousty API",
    description="API backend pour Ytasty Crousty",
    version="1.0.0",
)


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


    SHema db, looping,

