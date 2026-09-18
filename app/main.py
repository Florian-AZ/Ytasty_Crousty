"""Point d'entree de l'API Ytasty Crousty."""

from fastapi import FastAPI

app = FastAPI(
    title="Ytasty Crousty API",
    description="API backend du restaurant Ytasty Crousty",
    version="0.1.0",
)


@app.get("/health", tags=["health"])
def health() -> dict[str, str]:
    """Verifie que l'API repond."""
    return {"status": "ok"}
