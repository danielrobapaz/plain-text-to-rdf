class CustomException(Exception):
    def __init__(self, message: str = ""):
        self.message = message
        super().__init__(message)

class InvalidCommandLineUsage(CustomException):
    pass

class UnexistingFlag(CustomException):
    pass    