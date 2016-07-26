import struct
from math import cos, asin, sqrt, sin, atan2, pi


def f2i(float_):
    return struct.unpack('<Q', struct.pack('<d', float_))[0]

def f2h(float_):
    return hex(struct.unpack('<Q', struct.pack('<d', float_))[0])

def h2f(hex_):
    return struct.unpack('<d', struct.pack('<Q', int(hex_,16)))[0]


class LocationManager(object):
    """ Location Manager class for managing which coordinates will be used
    """

    def __init__(self, latitude=0.0, longitude=0.0, altitude=0.0):
        """ constructor to set location
        """
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude

    def get_latitude(self):
        """ @ return latitude as integer
        """
        return self.latitude

    def get_longitude(self):
        """ @return longitude as integer
        """
        return self.longitude

    def get_altitude(self):
        """ @return altitude 
        """  
        return self.altitude

    def get_lat_lng(self):
        return (self.latitude, self.longitude)

    def set_location(self, latitude, longitude, altitude):
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude


class Coordinates(object):

    # the length of one degree of latitude (and one degree of longitude at equator) in meters.
    DEGREE_DISTANCE_AT_EQUATOR = 111329.0
    # the radius of the earth in meters.
    EARTH_RADIUS = 6378137.0 # in meters
    # the length of one minute of latitude in meters, i.e. one nautical mile in meters.
    MINUTES_TO_METERS = 1852.0
    # the amount of minutes in one degree.
    DEGREE_TO_MINUTES = 60.0

    @staticmethod
    def distance_haversine_km(lat1, lon1, lat2, lon2):
        p = 0.017453292519943295
        a = 0.5 - cos((lat2 - lat1) * p) / 2 + cos(lat1 * p) * \
            cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
        return 12742 * asin(sqrt(a)) * 1000

    @staticmethod
    def distance_haversine_km_2(lat1, lon1, lat2, lon2):
        R = 6371 # Radius of the earth in km
        dLat = Coordinates.deg2rad(lat2 - lat1)
        dLon = Coordinates.deg2rad(lon2 - lon1)
        a = sin(dLat/2) * sin(dLat/2) + cos(Coordinates.deg2rad(lat1)) * cos(Coordinates.deg2rad(lat2)) *  sin(dLon/2) * sin(dLon/2)
        c = 2 * atan2(sqrt(a), sqrt(1-a))
        d = R * c # Distance in km
        return d

    @staticmethod
    def deg2rad(deg):
        return deg * (pi / 180)

    @staticmethod
    def rad2deg(rad):
        return rad * (180 / pi)

    """
    """
    @staticmethod
    def extrapolate(latitude, logitude, course, distance):
        crs = Coordinates.deg2rad(course)
        d12 = Coordinates.deg2rad(distance / Coordinates.MINUTES_TO_METERS / Coordinates.DEGREE_TO_MINUTES)

        lat1 = Coordinates.deg2rad(latitude)
        lon1 = Coordinates.deg2rad(logitude)

        lat = asin(sin(lat1) * cos(d12) + cos(lat1) * sin(d12) * cos(crs))
        dlon = atan2(sin(crs) * sin(d12) * cos(lat1), cos(d12) - sin(lat1) * sin(lat))
        lon = (lon1 + dlon + pi) % (2 * pi) - pi

        return (Coordinates.rad2deg(lat), Coordinates.rad2deg(lon))

    @staticmethod
    def angle_between_coords(lat1, lng1, lat2, lng2):
        # convert arguments to radians
        lat1 = Coordinates.deg2rad(lat1)
        lng1 = Coordinates.deg2rad(lng1)
        lat2 = Coordinates.deg2rad(lat2)
        lng2 = Coordinates.deg2rad(lng2)

        dLon = (lng2 - lng1)

        y = sin(dLon) * cos(lat2)
        x = cos(lat1) * sin(lat2) - sin(lat1) * cos(lat2) * cos(dLon)

        brng = atan2(y, x)
        brng = Coordinates.rad2deg(brng)
        brng = (brng + 360) % 360
        #brng = 360 - brng

        return round(brng);