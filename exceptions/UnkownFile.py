

class UnkownFile(Exception):
    def __init__(self, file):
        self.file = file

    def __str__(self):
        return f"Archivo no encontrado: {self.file}"