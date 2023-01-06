from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ArtistBase(BaseModel):
    ArtistId: Optional[int]
    Name: Optional[str]


class ArtistInDB(ArtistBase):
    ArtistId: Optional[int]
    Name: Optional[str]

    class Config:
        orm_mode = True


class AlbumBase(BaseModel):
    AlbumId: Optional[int]
    Title: Optional[str]
    ArtistId: Optional[int]


class AlbumInDB(AlbumBase):
    AlbumId: Optional[int]
    Title: Optional[str]
    ArtistId: Optional[int]

    class Config:
        orm_mode = True


class TrackBase(BaseModel):
    TrackId: Optional[int]
    Name: Optional[str]
    AlbumId: Optional[int]
    MediaTypeId: Optional[int]
    GenreId: Optional[int]
    Composer: Optional[str]
    Milliseconds: Optional[int]
    Bytes: Optional[int]
    UnitPrice: Optional[float]


class TrackInDB(TrackBase):
    TrackId: Optional[int]
    Name: Optional[str]
    AlbumId: Optional[int]
    MediaTypeId: Optional[int]
    GenreId: Optional[int]
    Composer: Optional[str]
    Milliseconds: Optional[int]
    Bytes: Optional[int]
    UnitPrice: Optional[float]

    class Config:
        orm_mode = True



class GenreBase(BaseModel):
    GenreId: Optional[int]
    Name: Optional[str]


class GenreInDB(GenreBase):
    GenreId: Optional[int]
    Name: Optional[str]

    class Config:
        orm_mode = True


class MediaTypeBase(BaseModel):
    MediaTypeId: Optional[int]
    Name: Optional[str]


class MediaTypeInDB(MediaTypeBase):
    MediaTypeId: Optional[int]
    Name: Optional[str]

    class Config:
        orm_mode = True
        
class TrackAux(TrackBase):
    TrackId: Optional[int]
    Name: Optional[str]
    AlbumId: Optional[int]
    MediaType: Optional[str]
    Genre: Optional[str]
    Composer: Optional[str]
    Milliseconds: Optional[int]
    Bytes: Optional[int]
    UnitPrice: Optional[float]


    class Config:
        orm_mode = True