import struct


def f2i(float):
    return struct.unpack('<Q', struct.pack('<d', float))[0]

def f2h(float):
    return hex(struct.unpack('<Q', struct.pack('<d', float))[0])

def h2f(hex):
    return struct.unpack('<d', struct.pack('<Q', int(hex,16)))[0]


""" Location Manager class for managing which coordinates will be used
"""
class LocationManager(object):

    """ constructor to set location
    """
    def __init__(self, latitude=0, longitude=0, altitude=0):
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude

    """ @ return latitude as integer
    """
    def get_latitude(self):
        return self.latitude

    """ @return longitude as integer
    """
    def get_longitude(self):
        return self.longitude

    """ @return altitude 
    """  
    def get_altitude(self):
        return self.altitude