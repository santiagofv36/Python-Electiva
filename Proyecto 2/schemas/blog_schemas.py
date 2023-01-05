from datetime import datetime
from typing import Optional, Text

from pydantic import BaseModel


class BlogBase(BaseModel):
    title: str | None
    author: Optional[str]
    content: Optional[Text]


# usado para crear el blog
class BlogCreate(BlogBase):
    title: str
    author: str
    content:Text


class BlogUpdate(BlogBase):
    title: Optional[str]
    author: Optional[str]
    content:Optional[Text]
    created_at: Optional[datetime]
    published_at: Optional[datetime]
    published: Optional[bool]


# usado para entregar un blog
class BlogInDB(BlogBase):
    id: int
    title: str
    author: str
    content:Text
    created_at: datetime
    published_at: datetime
    is_published: bool

    class Config:
        orm_mode = True