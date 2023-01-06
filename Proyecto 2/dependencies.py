from config_db import SessionLocal
from repositories.music_repository import MusicRepository

# función helper para obtener una session de la bd
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_music_repo():
    return MusicRepository()