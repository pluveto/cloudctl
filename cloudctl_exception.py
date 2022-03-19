class BadRequestException(Exception):
    """
    Exception raised when a bad parameter is passed to a function.
    """
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
    
class ServerInternalException(Exception):
    """
    Exception raised when a server internal error occurs.
    """
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message