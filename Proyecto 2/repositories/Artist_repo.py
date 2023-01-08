from typing import List

from sqlalchemy.orm import Session
from schemas.schemas import ArtistInDB, AlbumInDB, TrackInDB
from models.models import Artists, Albums, Tracks, Genres, MediaTypes


class ArtistRepo:

    '''
        Obtener todos los artistas
    '''

    async def get_all_artists(self, db: Session) -> List[ArtistInDB]:
        return db.query(Artists).all()

    '''
        Obtener todos los albumes de un artista
    '''

    async def get_all_albums_by_artist(self, db: Session, artist_id: int) -> List[AlbumInDB]:
        return db.query(Albums).filter(Albums.ArtistId == artist_id).all()


    '''
        Obtener todas las canciones de un artista
    '''
    async def get_all_tracks_by_artist(self, db: Session, artist_id: int) -> List[TrackInDB]:
        return db.query(Tracks
            ).join(
            Albums, Tracks.AlbumId == Albums.AlbumId
            ).filter(Albums.ArtistId == artist_id).all()
    