

class EmptyFile(Exception):
    
    def __init__(self,file):
        self.file = file

    def __str__(self):
        return f'El archivo {self.file} esta vacio'