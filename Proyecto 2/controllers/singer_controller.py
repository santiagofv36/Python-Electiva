from typing import List
from dependencies import get_db

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from repositories.Artist_repo import ArtistRepo

from schemas.schemas import AlbumInDB, ArtistInDB, TrackInDB



router = APIRouter(
    tags=["Singer"]
)

'''
    Ruta para obtener las canciones de un artista
'''

@router.get("/singer/{id}", response_model=List[TrackInDB], status_code=status.HTTP_200_OK)
async def get_tracks_by_artist(
        id: int, 
        db: Session = Depends(get_db), 
        artist_repo: ArtistRepo = Depends(ArtistRepo), ) -> List[TrackInDB]:

    tracks = await artist_repo.get_all_tracks_by_artist(db=db, artist_id=id)
    if tracks is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Track no encontrado")
    return tracks

'''
    Ruta para obtener todos los artistas
'''

@router.get("/singers", response_model=List[ArtistInDB], status_code=status.HTTP_200_OK)
async def get_all_artists(
        db: Session = Depends(get_db), 
        artist_repo: ArtistRepo = Depends(ArtistRepo), ) -> List[ArtistInDB]:

    artists = await artist_repo.get_all_artists(db=db)
    if not artists:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Artista no encontrado")
    return artists

'''
    Ruta para obtener todos los albumes de un artista
'''

@router.get("/singers/{id}", response_model=List[AlbumInDB], status_code=status.HTTP_200_OK)
async def get_albums_by_artist_id(id: int,
        db: Session = Depends(get_db), 
        artist_repo: ArtistRepo = Depends(ArtistRepo), ) -> List[AlbumInDB]:

    albums = await artist_repo.get_all_albums_by_artist(db=db, artist_id=id)
    if not albums:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Album no encontrado")
    return albums
