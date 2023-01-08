from config_db import SessionLocal

'''
    Funcion que retorna una sesion de la base de datos
'''
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
