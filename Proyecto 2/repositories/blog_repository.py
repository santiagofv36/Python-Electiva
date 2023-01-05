from datetime import datetime
from typing import List

from sqlalchemy.orm import Session

from models.blog_models import Blogs
from schemas.blog_schemas import BlogCreate ,BlogInDB, BlogUpdate

class BlogRepo:

    # create un blog
    async def create_blog(self, *, db: Session, new_blog: BlogCreate) -> BlogInDB:
        blog = Blogs(
            title=new_blog.title, 
            author=new_blog.author,
            content=new_blog.content,
            created_at=datetime.now(),
            published_at = datetime.now(),
            is_published = True 
        )

        db.add(blog)
        db.commit()
        db.refresh(blog)
        return blog

    # obtiene todos los blogs
    async def get_all_blogs(self, db: Session) -> List[BlogInDB]:
        blog_list: List[BlogInDB] = db.query(Blogs).all()
        return blog_list

    # obtiene un blog en particular
    async def get_blog_by_id(self, *, id:int, db: Session) -> BlogInDB:
        blog: BlogInDB = db.query(Blogs).get(id)
        return blog 

    # actualiza un blog
    async def update_blog_by_id(self, *, id: int, blog_update: BlogUpdate, db: Session) -> BlogInDB:
        blog_db = self.get_blog_by_id(id=id, db=db)
        if not blog_db:
            return None

        blog_data = blog_update.dict(exclude_unset=True)
        for key, value in blog_data.items():
            setattr(blog_db, key, value)
        db.add(blog_db)
        db.commit()
        db.refresh(blog_db)
        return blog_db

    #elimina un blog
    async def delete_blog_by_id(self, *, id=int, db: Session) -> int | None:
        blogdb = self.get_blog_by_id(id=id, db=db)
        if not blogdb:
            return None

        id = blogdb.id
        db.delete(blogdb)
        db.commit()

        return id