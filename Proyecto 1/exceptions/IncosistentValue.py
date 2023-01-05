

class IncosistentValue(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Hay datos inconsistentes en el archivo:  {self.value}'