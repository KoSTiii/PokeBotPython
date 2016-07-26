

""" Exception class for error exception in
Login to pokemon servers
"""
class LoginFailedException(Exception):
    
    def __init__(self, message):
        """
        """
        Exception.__init__(self)
        self.message = message
    
    def __str__(self):
        """
        """
        return repr(self.message)


class NotLoggedInException(Exception):
    """
    """
    
    def __init__(self, message):
        """
        """
        Exception.__init__(self)
        self.message = message
    
    def __str__(self):
        """
        """
        return repr(self.message)


class InvalidAuthenticationException(Exception):
    """
    """

    def __init__(self, message):
        """
        """
        Exception.__init__(self)
        self.message = message
    
    def __str__(self):
        """
        """
        return repr(self.message)


class IllegalStateException(Exception):
    """
    """

    def __init__(self, message):
        """
        """
        Exception.__init__(self)
        self.message = message
    
    def __str__(self):
        """
        """
        return repr(self.message)


class ObjectNotInitialized(Exception):
    """
    """

    def __init__(self, message):
        """
        """
        Exception.__init__(self)
        self.message = message
    
    def __str__(self):
        """
        """
        return repr(self.message)


class ObjectIsWrongTypeException(Exception):
    """
    """

    def __init__(self, message):
        """
        """
        Exception.__init__(self)
        self.message = message
    
    def __str__(self):
        """
        """
        return repr(self.message)