import struct

def f2i(float):
    return struct.unpack('<Q', struct.pack('<d', float))[0]

def f2h(float):
  return hex(struct.unpack('<Q', struct.pack('<d', float))[0])

def h2f(hex):
  return struct.unpack('<d', struct.pack('<Q', int(hex,16)))[0]


class LocationManager():

    def __init__(self):
        self.longitude = None
        self.latitude = None
        self.altitude = None

    def __init__(self, latitude, longitude, altitude):
        self.longitude = longitude
        self.latitude = latitude
        self.altitude = altitude

    def get_longitude(self):
        return f2i(self.longitude)

    def set_longitude(self, longitude):
        self.longitude = longitude

    def get_latitude(self):
        return f2i(self.latitude)

    def set_latitude(self, latitude):
        self.latitude = latitude

    def get_altitude(self):
        return self.altitude

    def set_altitude(self, altitude):
        self.altitude = altitude



