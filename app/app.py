from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.database.connection import engine
from app.database.models import Base
from app.routers.redirect import router as redirect_router
from app.routers.url import router as url_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Encurtador de URL",
    description="API para encurtamento de links e rastreamento de acessos",
    version="1.0.0"
)

STATIC_DIR = Path(__file__).parent / "static"

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

@app.get("/", include_in_schema=False)
def index():
    """Serve a interface web do encurtador."""
    return FileResponse(STATIC_DIR / "index.html")


@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    """Serve o favicon da aplicação."""
    return FileResponse(STATIC_DIR / "favicon.svg", media_type="image/svg+xml")


app.include_router(url_router)
app.include_router(redirect_router)