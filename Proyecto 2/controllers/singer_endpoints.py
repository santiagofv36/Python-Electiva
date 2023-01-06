from typing import List
from dependencies import get_db, get_music_repo

from fastapi import APIRouter, Body, Depends, HTTPException, Path, status
from sqlalchemy.orm import Session
from repositories.music_repository import MusicRepository

from schemas.schemas import TrackInDB



router = APIRouter(
    prefix="/singer",
    tags=["Singer"]
)

@router.get("/{id}", response_model=List[TrackInDB], status_code=status.HTTP_200_OK)
async def get_tracks_by_artist(
        id: int, 
        db: Session = Depends(get_db), 
        music_repo: MusicRepository = Depends(get_music_repo), ) -> List[TrackInDB]:

    tracks = await music_repo.get_all_tracks_by_artist(db=db, artist_id=id)
    if tracks is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Track no encontrado")
    return tracks


