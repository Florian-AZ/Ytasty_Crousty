# Ytasty Crousty — API

Backend FastAPI + PostgreSQL + SQLAlchemy, géré avec uv.

## Lancer le projet

```bash
docker compose up --build
```

- API : http://localhost:8000/health
- Swagger : http://localhost:8000/docs
- OpenAPI : http://localhost:8000/openapi.json

Sans Docker (nécessite un PostgreSQL local et un fichier `.env`,
voir `.env.example`) :

```bash
uv sync
uv run uvicorn app.main:app --reload
```

## Arborescence

```
app/
├── main.py                  crée l'app, /health, branche les routers
├── core/
│   ├── config.py            variables d'environnement (.env)
│   └── security.py          hash des mots de passe + JWT
├── database/
│   ├── database.py          engine SQLAlchemy + get_db()
│   └── models/              les tables (users, restaurants, products...)
├── schemas/                 schémas Pydantic (entrées / sorties de l'API)
└── routers/                 endpoints, un fichier par ressource
```

Pour ajouter une fonctionnalité : son modèle dans `database/models/`,
ses schémas dans `schemas/`, ses endpoints dans `routers/`, puis on
branche le router dans `main.py` avec `app.include_router(...)`.

## Configuration

Copier `.env.example` vers `.env` et remplir les valeurs.
Aucun secret ne doit être commité : le `.env` est ignoré par Git.

| Variable           | Rôle                                    |
| ------------------ | --------------------------------------- |
| DATABASE_URL       | connexion PostgreSQL                    |
| JWT_SECRET_KEY     | clé de signature des tokens JWT         |
| JWT_ALGORITHM      | algorithme de signature (HS256)         |
| JWT_EXPIRE_MINUTES | durée de validité d'un token en minutes |

## À venir (voir les issues GitHub)

Modèles conformes au contrat, seed (admin + 3 restaurants),
authentification JWT, users, restaurants, products, orders, déploiement.
