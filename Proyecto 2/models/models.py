from sqlalchemy import Boolean, Column, DateTime, Integer, String 

from config_db import Base
'''
    Modelo de la tabla Albums
'''
class Albums(Base):
    __tablename__ = "albums"
    AlbumId = Column(Integer, primary_key=True, index=True)
    Title = Column(String)
    ArtistId = Column(Integer)

'''
    Modelo de la tabla Artists
'''

class Artists(Base):
    __tablename__ = "artists"
    ArtistId = Column(Integer, primary_key=True, index=True)
    Name = Column(String)
'''
    Modelo de la tabla Tracks
'''
class Tracks(Base):
    __tablename__ = "tracks"
    TrackId = Column(Integer, primary_key=True, index=True)
    Name = Column(String)
    AlbumId = Column(Integer)
    MediaTypeId = Column(Integer)
    GenreId = Column(Integer)
    Composer = Column(String)
    Milliseconds = Column(Integer)
    Bytes = Column(Integer)
    UnitPrice = Column(Integer)

'''
    Modelo de la tabla Genres
'''
class Genres(Base):
    __tablename__ = "genres"
    GenreId = Column(Integer, primary_key=True, index=True)
    Name = Column(String)

'''
    Modelo de la tabla MediaTypes
'''

class MediaTypes(Base):
    __tablename__ = "media_types"
    MediaTypeId = Column(Integer, primary_key=True, index=True)
    Name = Column(String)