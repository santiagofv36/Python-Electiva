from typing import List

from fastapi import APIRouter, Body, Depends, HTTPException, Path, status
from sqlalchemy.orm import Session

from dependencies import get_blog_repo, get_db
from repositories.blog_repository import BlogRepo
from schemas.blog_schemas import BlogCreate ,BlogInDB, BlogUpdate

router = APIRouter(
    prefix="/blogs",
    tags=["Blogs"]
)

@router.post("/", response_model=BlogInDB, status_code=status.HTTP_201_CREATED)
async def create_blog(
    new_blog: BlogCreate = Body(..., embed=True),
    db: Session = Depends(get_db),
    blog_repo: BlogRepo = Depends(get_blog_repo)
) -> BlogInDB:
    return await blog_repo.create_blog(db=db, new_blog=new_blog)

@router.get("/", response_model=List[BlogInDB], status_code=status.HTTP_200_OK)
async def get_all_blogs(
    db: Session = Depends(get_db),
    blog_repo: BlogRepo = Depends(get_blog_repo),
) -> List[BlogInDB] :
    return await blog_repo.get_all_blogs(db=db)

@router.get("/{id}", response_model=BlogInDB, status_code=status.HTTP_200_OK)
async def get_one_blog(
    id: int, 
    db: Session = Depends(get_db),
    blog_repo: BlogRepo = Depends(get_blog_repo), 
) -> BlogInDB:
    blog =  await blog_repo.get_blog_by_id(id=id, db=db )

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return blog

@router.put("/{id}", response_model=BlogInDB)
async def update_one_blog(
    id: int = Path(..., ge=1, title="el id del blog a actualizar"),
    blog_update: BlogUpdate = Body(..., embed=True),
    db: Session = Depends(get_db),
    blog_repo: BlogRepo = Depends(get_blog_repo), 
) -> BlogInDB:
    blog =  await blog_repo.update_blog_by_id(id=id, blog_update=blog_update, db=db)

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return blog

@router.delete("/{id}/")
async def delete_one_blog(
    id: int, db: Session = Depends(get_db),
    blog_repo: BlogRepo = Depends(get_blog_repo),
) -> int:
    delete_id =  await blog_repo.delete_blog_by_id(id=id, db=db)

    if not delete_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return {"delete_id" : delete_id}