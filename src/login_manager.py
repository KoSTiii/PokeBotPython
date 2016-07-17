

#
#   Login class manager
#
class LoginManager():

    LoginType = ["PTC", "Google"]

    # constructor
    def __init__(self, type, username, password):
        if type not in LoginType:
            type = "PTC"
        
        self.type = "PTC"
        self.username = username
        self.password = password

    # login to server
    def login(self):
        pass

    # retrurn accessToken
    def getAccessToken(self):
        return self.accessToken