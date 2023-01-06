from datetime import datetime
from typing import List

from sqlalchemy.orm import Session
from schemas.schemas import ArtistInDB, AlbumInDB, TrackInDB, TrackAux
from models.models import Artists, Albums, Tracks, Genres, MediaTypes




class MusicRepository:


    '''
        Obtener todos los artistas
    '''

    async def get_all_artists(self, db: Session) -> List[ArtistInDB]:
        return db.query(Artists).all()

    '''
        Obtener un artista por su id
    '''

    async def get_artist_by_id(self, db: Session, artist_id: int) -> ArtistInDB:
        return db.query(Artists).filter(Artists.ArtistId == artist_id).first()

    '''
        Obtener todos los albumes de un artista
    '''

    async def get_all_albums_by_artist(self, db: Session, artist_id: int) -> List[AlbumInDB]:
        return db.query(Albums).filter(Albums.ArtistId == artist_id).all()

    '''
        Obtener todas las canciones de un album 
    '''

    async def get_all_tracks_by_album(self, db: Session, album_id: int) -> List[TrackInDB]:
        return db.query(Tracks).filter(Tracks.AlbumId == album_id).all()

    '''
        Obtener todas las canciones de un artista
    '''
    async def get_all_tracks_by_artist(self, db: Session, artist_id: int) -> List[TrackInDB]:
        return db.query(Tracks
            ).join(
            Albums, Tracks.AlbumId == Albums.AlbumId
            ).filter(Albums.ArtistId == artist_id).all()

    '''
        Obtener detalles de una cancion por su id
    '''
    async def get_track_by_id(self, db: Session, track_id: int) -> TrackInDB:
        track : TrackInDB = db.query(Tracks).get(track_id)
        genre : Genres = db.query(Genres).get(track.GenreId)
        media_type : MediaTypes = db.query(MediaTypes).get(track.MediaTypeId)
        track.Genre = str(genre.Name) 
        track.MediaType = str(media_type.Name)
        return track







    
