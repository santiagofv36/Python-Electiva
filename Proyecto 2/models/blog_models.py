from sqlalchemy import Boolean, Column, DateTime, Integer, String 

from config_db import Base

class Blogs(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    author = Column(String)
    content = Column(String)
    created_at = Column(DateTime)
    published_at = Column(DateTime)
    is_published = Column(Boolean, default=True)