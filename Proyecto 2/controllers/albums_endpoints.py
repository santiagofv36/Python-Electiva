from typing import List
from dependencies import get_db, get_music_repo

from fastapi import APIRouter, Body, Depends, HTTPException, Path, status
from sqlalchemy.orm import Session
from repositories.music_repository import MusicRepository

from schemas.schemas import TrackInDB



router = APIRouter(
    prefix="/albums",
    tags=["Albums"]
)

@router.get("/{id}", response_model=List[TrackInDB], status_code=status.HTTP_200_OK)
async def get_albums_by_artist_id(id: int, 
        db: Session = Depends(get_db), 
        music_repo: MusicRepository = Depends(get_music_repo), ) -> List[TrackInDB]:

    albums = await music_repo.get_all_tracks_by_album(db=db, album_id=id)
    if albums is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Album no encontrado")
    return albums


