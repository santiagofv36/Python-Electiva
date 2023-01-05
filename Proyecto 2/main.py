from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config_db import Base, engine
from controllers.blog_routes import router as blog_router

def get_application():

    # crea la base de datos
    Base.metadata.create_all(bind=engine)

    app = FastAPI(title="API Blog demo", version="1.0.0")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(blog_router, prefix="/api/v1")
    return app

app = get_application()

@app.get("/")
def home() -> dict:
    return {"mensaje": "Bienvenido a la aplicacion CRUD de Demo"}