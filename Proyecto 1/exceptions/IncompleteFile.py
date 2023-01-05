

class IncompleteFile(Exception):
    def __init__(self, file, message):
        self.file = file
        self.message = message

    def __str__(self):
        return f"El archivo: {self.message} tiene datos incompletos"