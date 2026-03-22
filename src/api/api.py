from fastapi import FastAPI
from .routes import router

def create_app() -> FastAPI:
    app = FastAPI(title="Agent AI Lab API")
    app.include_router(router)
    return app
