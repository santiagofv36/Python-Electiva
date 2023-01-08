from typing import List
from dependencies import get_db

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from repositories.TrackRepo import TrackRepo

from schemas.schemas import TrackAux



router = APIRouter(
    prefix="/song",
    tags=["Song"]
)

'''
    Ruta para obtener todos los detalles de una cancion por su id
'''

@router.get("/{id}", response_model=TrackAux, status_code=status.HTTP_200_OK)
async def get_song_by_id(id: int,
        db: Session = Depends(get_db), 
        track_repo: TrackRepo = Depends(TrackRepo), ) -> TrackAux:

    song = await track_repo.get_track_by_id(db=db, track_id=id)
    if song is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cancion no encontrada")
    return song

