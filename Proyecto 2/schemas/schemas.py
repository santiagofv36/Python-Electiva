from datetime import datetime
from typing import Optional

from pydantic import BaseModel


'''
    Clases para los modelos de la base de datos
'''

'''
    Clase para manejar los artistas a nivel de dominio
'''

class ArtistBase(BaseModel):
    ArtistId: Optional[int]
    Name: Optional[str]

'''
    Clase para manejar los artistas a nivel de base de datos
'''
class ArtistInDB(ArtistBase):
    ArtistId: Optional[int]
    Name: Optional[str]

    class Config:
        orm_mode = True

'''
    Clase para manejar los albumes a nivel de dominio
'''

class AlbumBase(BaseModel):
    AlbumId: Optional[int]
    Title: Optional[str]
    ArtistId: Optional[int]

'''
    Clase para manejar los albumes a nivel de base de datos
'''

class AlbumInDB(AlbumBase):
    AlbumId: Optional[int]
    Title: Optional[str]
    ArtistId: Optional[int]

    class Config:
        orm_mode = True

'''
    Clase para manejar las canciones a nivel de dominio
'''
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

'''
    Clase para manejar las canciones a nivel de base de datos
'''
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

'''
    Clase para manejar los generos a nivel de dominio
'''

class GenreBase(BaseModel):
    GenreId: Optional[int]
    Name: Optional[str]

'''
    Clase para manejar los generos a nivel de base de datos
'''
class GenreInDB(GenreBase):
    GenreId: Optional[int]
    Name: Optional[str]

    class Config:
        orm_mode = True

'''
    Clase para manejar los tipos de medios a nivel de dominio
'''
class MediaTypeBase(BaseModel):
    MediaTypeId: Optional[int]
    Name: Optional[str]


'''
    Clase para manejar los tipos de medios a nivel de base de datos
'''

class MediaTypeInDB(MediaTypeBase):
    MediaTypeId: Optional[int]
    Name: Optional[str]

    class Config:
        orm_mode = True


'''
    Clase para manejar la respuesta de las canciones, en donde se incluye el nombre del genero y del tipo de medio a nivel de base de datos
''' 

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