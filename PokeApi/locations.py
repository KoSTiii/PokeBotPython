

""" Location Manager class for managing which coordinates will be used
"""
class LocationManager(object):

    """ constructor to set location
    """
    def __init__(self, latitude=None, longitude=None, altitude=0):
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude