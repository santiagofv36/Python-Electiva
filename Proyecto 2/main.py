from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config_db import Base, engine

from controllers.singer_endpoints import router as singer
from controllers.albums_endpoints import router as albums
from controllers.singers_endpoints import router as singers
from controllers.track_endpoints import router as tracks


def get_application():

    # crea la base de datos
    Base.metadata.create_all(bind=engine)

    app = FastAPI(title="Music Store Parcial 2",
        description="Realizado por Santiago Figueroa",
        version="1.0.0"
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(singer, prefix="/music-store/api/v1")
    app.include_router(albums, prefix="/music-store/api/v1")
    app.include_router(singers, prefix="/music-store/api/v1")
    app.include_router(tracks, prefix="/music-store/api/v1")


    return app

app = get_application()

@app.get("/")
def home() -> dict:
    return {"Mensaje" : "Bienvenido a la API de Music Store"}