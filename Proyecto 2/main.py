from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config_db import Base, engine

from controllers.singer_controller import router as singer
from controllers.albums_controller import router as albums
from controllers.track_controller import router as tracks


def get_application():

    '''
        Crea la base de datos
    '''
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

    '''
        Rutas de la API que corresponden a los controladores de cada entidad
    '''

    app.include_router(singer, prefix="/music-store/api/v1")
    app.include_router(albums, prefix="/music-store/api/v1")
    app.include_router(tracks, prefix="/music-store/api/v1")


    return app

app = get_application()

'''
    Ruta de inicio
'''

@app.get("/")
def home() -> dict:
    return {"Mensaje" : "Bienvenido a la API de Music Store"}