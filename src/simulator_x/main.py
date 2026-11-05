"""FastAPI app and local development server."""
import uvicorn
from fastapi import FastAPI
from simulator_x import __version__
from simulator_x.config import settings
from simulator_x.database.db import init_db
from simulator_x.api.routes import router
def create_app():
    app = FastAPI(title=settings.app_name, version=__version__, description="Offline SIM-behaviour sandbox using synthetic test data only.")
    app.include_router(router)
    @app.on_event("startup")
    def startup(): init_db()
    @app.get("/health", tags=["system"])
    def health(): return {"status": "ok", "service": settings.app_name, "version": __version__, "mode": "offline-simulation"}
    return app
app = create_app()
def run(): uvicorn.run("simulator_x.main:app", host=settings.host, port=settings.port, reload=settings.app_env == "development")
