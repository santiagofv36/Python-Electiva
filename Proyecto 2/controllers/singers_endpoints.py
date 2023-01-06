from typing import List
from dependencies import get_db, get_music_repo

from fastapi import APIRouter, Body, Depends, HTTPException, Path, status
from sqlalchemy.orm import Session
from repositories.music_repository import MusicRepository

from schemas.schemas import TrackInDB, ArtistInDB, AlbumInDB



router = APIRouter(
    prefix="/singers",
    tags=["Singers"]
)

@router.get("/", response_model=List[ArtistInDB], status_code=status.HTTP_200_OK)
async def get_all_artists(
        db: Session = Depends(get_db), 
        music_repo: MusicRepository = Depends(get_music_repo), ) -> List[ArtistInDB]:

    artists = await music_repo.get_all_artists(db=db)
    if artists is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Artista no encontrado")
    return artists

@router.get("/{id}", response_model=List[AlbumInDB], status_code=status.HTTP_200_OK)
async def get_albums_by_artist_id(id: int,
        db: Session = Depends(get_db), 
        music_repo: MusicRepository = Depends(get_music_repo), ) -> List[AlbumInDB]:

    albums = await music_repo.get_all_albums_by_artist(db=db, artist_id=id)
    if albums is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Album no encontrado")
    return albums


