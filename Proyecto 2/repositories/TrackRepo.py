from models.models import Tracks, Genres, MediaTypes
from typing import List
from sqlalchemy.orm import Session
from schemas.schemas import  TrackInDB


class TrackRepo:

    '''
        Obtener detalles de una cancion por su id
    '''
    async def get_track_by_id(self, db: Session, track_id: int) -> TrackInDB:
        track : TrackInDB = db.query(Tracks).get(track_id)
        if track:
            genre : Genres = db.query(Genres).get(track.GenreId)
            media_type : MediaTypes = db.query(MediaTypes).get(track.MediaTypeId)
            track.Genre = str(genre.Name) 
            track.MediaType = str(media_type.Name) 
        return track