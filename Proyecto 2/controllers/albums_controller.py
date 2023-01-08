from typing import List
from dependencies import get_db

from fastapi import APIRouter, Body, Depends, HTTPException, Path, status
from sqlalchemy.orm import Session
from repositories.AlbumRepo import AlbumRepo

from schemas.schemas import TrackInDB



router = APIRouter(
    prefix="/albums",
    tags=["Albums"]
)

'''
    Ruta para obtener todas las canciones de un album
'''

@router.get("/{id}", response_model=List[TrackInDB], status_code=status.HTTP_200_OK)
async def get_albums_by_artist_id(id: int, 
        db: Session = Depends(get_db), 
        album_repo: AlbumRepo = Depends(AlbumRepo), ) -> List[TrackInDB]:

    albums = await album_repo.get_all_tracks_by_album(db=db, album_id=id)
    if not albums:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Album no encontrado")
    return albums


