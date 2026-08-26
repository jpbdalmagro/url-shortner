from fastapi import FastAPI
from app.database.connection import engine, Base
from app.routers import url, redirect

# Cria as tabelas no banco de dados caso não existam
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="URL Shortener API",
    description="API simples e eficiente para encurtamento de URLs e análise de acessos.",
    version="1.0.0",
)

# Registro dos roteadores
app.include_router(url.router)
app.include_router(redirect.router)


@app.get("/", tags=["Health Check"])
def root():
    return {
        "message": "URL Shortener API está online!",
        "docs": "/docs",
        "redoc": "/redoc"
    }

