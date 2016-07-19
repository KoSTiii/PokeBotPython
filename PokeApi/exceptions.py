

""" Exception class for error exception in
Login to pokemon servers
"""
class LoginFailedException(Exception):
    
    def __init__(self, message):
        self.message = message
    
    def __str__(self):
        return repr(self.message)


"""
"""
class InvalidAuthenticationException(Exception):

    def __init__(self, message):
        self.message = message
    
    def __str__(self):
        return repr(self.message)


"""
"""
class IllegalStateException(Exception):

    def __init__(self, message):
        self.message = message
    
    def __str__(self):
        return repr(self.message)