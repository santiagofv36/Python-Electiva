from typing import List
from models.models import Tracks
from sqlalchemy.orm import Session

from schemas.schemas import TrackInDB



class AlbumRepo:
    '''
        Obtener todas las canciones de un album 
    '''
    async def get_all_tracks_by_album(self, db: Session, album_id: int) -> List[TrackInDB]:
        return db.query(Tracks).filter(Tracks.AlbumId == album_id).all()
