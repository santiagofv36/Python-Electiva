

class NotTxt(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f'El archivo: {self.message} no es un archivo de texto'