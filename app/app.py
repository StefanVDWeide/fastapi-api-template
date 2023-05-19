from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import users, posts, auth


def create_app() -> FastAPI:
    app = FastAPI(title="Fastapi Template")

    app.include_router(users.router)
    app.include_router(posts.router)
    app.include_router(auth.router)

    # For local development
    origins = [
        "http://localhost:3000",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Generic health route to sanity check the API
    @app.get("/health")
    async def health() -> str:
        return "ok"

    return app
