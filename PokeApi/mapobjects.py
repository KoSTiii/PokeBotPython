"""
"""

import struct
import time

from google.protobuf.internal import encoder
from geopy.geocoders import GoogleV3
from s2sphere import CellId, LatLng, Cell

from POGOProtos.Networking import Requests_pb2, Responses_pb2
from POGOProtos.Networking.Requests import Messages_pb2
from PokeApi.requesthandler import RequestHandler
from PokeApi.serverrequest import ServerRequest
from PokeApi.locations import LocationManager, f2i

""" Cell id level settings
"""
# S2 algorith cell level
S2_CELL_LEVEL = 15


def get_cellid(lat, long):
    origin = CellId.from_lat_lng(LatLng.from_degrees(lat, long)).parent(S2_CELL_LEVEL)
    walk = [origin.id()]

    # 10 before and 10 after
    next = origin.next()
    prev = origin.prev()
    for i in range(10):
        walk.append(prev.id())
        walk.append(next.id())
        next = next.next()
        prev = prev.prev()
    return sorted(walk)


def get_neighbours(lat, long):
    """ dobi krog okoli centra tocke
    """
    # ns = north east, ew = east west (ratio between 1 feet and degree) 
    # its different on diferent places on earth (sphere)!!
    ns = 0.0025
    ew = 0.0025
    walk = []
    for i in range(-2, 3):
        for j in range(-2, 3):
            thiscell = CellId.from_lat_lng(LatLng.from_degrees(lat + ns*i, long + ew*j)).parent(S2_CELL_LEVEL)
            if abs(i * j) < 4:
                walk.append(thiscell.id())
    return sorted(walk)


def get_neighbours_circular(lat, lng):
    """ Get neigbours in circular pattern
    """
    origin = CellId.from_lat_lng(LatLng.from_degrees(lat, lng)).parent(S2_CELL_LEVEL)
    neighbors = {origin.id()}

    edge_neighbors = origin.get_edge_neighbors()
    surrounding_neighbors = [
        edge_neighbors[0],                          # North neighbor
        edge_neighbors[0].get_edge_neighbors()[1],  # North-east neighbor
        edge_neighbors[1],                          # East neighbor
        edge_neighbors[2].get_edge_neighbors()[1],  # South-east neighbor
        edge_neighbors[2],                          # South neighbor
        edge_neighbors[2].get_edge_neighbors()[3],  # South-west neighbor
        edge_neighbors[3],                          # West neighbor
        edge_neighbors[0].get_edge_neighbors()[3],  # North-west neighbor
    ]

    for cell in surrounding_neighbors:
        neighbors.add(cell.id())
        for cell2 in cell.get_edge_neighbors():
            neighbors.add(cell2.id())

    return neighbors
