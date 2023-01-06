from typing import List
from dependencies import get_db, get_music_repo

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from repositories.music_repository import MusicRepository

from schemas.schemas import TrackAux, TrackInDB



router = APIRouter(
    prefix="/song",
    tags=["Song"]
)

@router.get("/{id}", response_model=TrackAux, status_code=status.HTTP_200_OK)
async def get_song_by_id(id: int,
        db: Session = Depends(get_db), 
        music_repo: MusicRepository = Depends(get_music_repo), ) -> TrackAux:

    song = await music_repo.get_track_by_id(db=db, track_id=id)
    if song is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cancion no encontrada")
    return song

