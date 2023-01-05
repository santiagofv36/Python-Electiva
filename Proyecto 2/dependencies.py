from config_db import SessionLocal
from repositories.blog_repository import BlogRepo

# función helper para obtener una session de la bd
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_blog_repo():
    return BlogRepo()