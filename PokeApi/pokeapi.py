import time
import logging
import importlib

from PokeApi import exceptions, mapobjects
from PokeApi.auth import PTCLogin, Auth
from PokeApi.requesthandler import RequestHandler
from PokeApi.serverrequest import ServerRequest, to_camel_case
from PokeApi.auth import Auth
from PokeApi.locations import LocationManager, f2i
from POGOProtos.Networking.Envelopes_pb2 import AuthTicket, ResponseEnvelope, RequestEnvelope, Unknown6
from POGOProtos.Networking import Requests_pb2
from POGOProtos.Networking.Requests import Messages_pb2
#data imports
from PokeApi.data import DataPlayer

from google.protobuf.internal.containers import RepeatedScalarFieldContainer


class PokeApi(object):

    def __init__(self, auth, location):
        """
        """
        self.logger = logging.getLogger(__name__)
        self.auth = auth
        self.request_handler = RequestHandler(auth)
        self.location_manager = location

        self.request_handler.set_location(self.location_manager)

    def __getattr__(self, func):
        """ Tole ful dober zgleda. The magic function
        """
        def function(**kwargs):
            name = func.upper()
            requestTypeValue = Requests_pb2.RequestType.Value(name)
            newReq = ServerRequest(requestTypeValue)

            if kwargs:
                camelCaseMessageName = "".join([to_camel_case(name), 'Message'])
                class_ = getattr(importlib.import_module("POGOProtos.Networking.Requests.Messages_pb2"), camelCaseMessageName)
                reqMessage = class_()
                # add parameters to message class
                for key, value in kwargs.items():
                    if not hasattr(reqMessage, key):
                        raise AttributeError
                    
                    #import pdb; pdb.set_trace()
                    attr = getattr(reqMessage, key)
                    if isinstance(attr, RepeatedScalarFieldContainer):
                        attr.extend(value)
                    else:
                        setattr(reqMessage, key, value)

                self.logger.debug("Arguments of '%s': \n\r%s", name, kwargs)
                newReq.set_request_message(reqMessage)
            
            self.request_handler.add_request(newReq)
            self.logger.debug("Adding '%s' to RequestHandler request", name)
            return self
   
        self.logger.debug('__getattr__ with name: ' + func)
        if func.upper() in Requests_pb2.RequestType.keys():
            return function
        else:
            raise AttributeError

    def send_requests(self):
        """ send requests
        """
        return self.request_handler.send_requests()

    def execute_heartbeat(self):
        """ @retruns [player_data, hatched_egg, inventory_data, check_awarded_badges, get_map_objects]
        """
        self.get_player()
        self.get_hatched_eggs()
        self.get_inventory()
        self.check_awarded_badges()
        self.add_get_map_objects_request()
        return self.send_requests()

    def get_profile(self):
        """
        """
        player = ServerRequest(Requests_pb2.GET_PLAYER)
        inv = ServerRequest(Requests_pb2.GET_INVENTORY)
        eggs = ServerRequest(Requests_pb2.GET_HATCHED_EGGS)
        settMessage = Messages_pb2.DownloadSettingsMessage()
        settMessage.hash = '05daf51635c82611d1aac95c0b051d3ec088a930'
        sett = ServerRequest(Requests_pb2.DOWNLOAD_SETTINGS, settMessage)
        badges = ServerRequest(Requests_pb2.CHECK_AWARDED_BADGES)
        
        self.request_handler.add_request(player)
        self.request_handler.add_request(inv)
        self.request_handler.add_request(eggs)
        self.request_handler.add_request(sett)
        self.request_handler.add_request(badges)

        ret = self.request_handler.send_requests()
        return ret #[player.get_structured_data(), inv.get_structured_data(), eggs.get_structured_data(), sett.get_structured_data(), badges.get_structured_data()]


    def _map_object_request(self, cellids):
        """ Map object request to the server
        @return object of GetMapObjectResponse
        """
        # create mesasge
        mapObjectMessage = Messages_pb2.GetMapObjectsMessage()
        mapObjectMessage.cell_id.extend(cellids)
        mapObjectMessage.since_timestamp_ms.extend([0] * len(cellids))
        mapObjectMessage.latitude = self.location_manager.get_latitude() #f2i(self.location_manager.get_latitude())
        mapObjectMessage.longitude = self.location_manager.get_longitude() #f2i(self.location_manager.get_longitude())

        # create server request
        mapObjects = ServerRequest(Requests_pb2.GET_MAP_OBJECTS, mapObjectMessage)
        self.request_handler.add_request(mapObjects)
        
        # return response
        mapObjectResponse = self.request_handler.send_requests()
        return mapObjectResponse


    def get_all_map_objects(self):
        """ get all map objects from server
        """
        # get cells id
        parentCells = mapobjects.get_neighbours_circular(self.location_manager.get_latitude(), self.location_manager.get_longitude())
        #parentCells = mapobjects.get_cellid(self.location_manager.get_latitude(), self.location_manager.get_longitude())
        mapObjectResponse = self._map_object_request(parentCells)
        return mapObjectResponse

    def add_get_map_objects_request(self):
        parentCells = mapobjects.get_neighbours_circular(self.location_manager.get_latitude(), self.location_manager.get_longitude())
        self.get_map_objects(cell_id=parentCells,
                             since_timestamp_ms=[0]*21,
                             latitude=self.location_manager.get_latitude(),
                             longitude=self.location_manager.get_longitude())

    def set_position(self, latitude, longitude, altitude):
        """ Set position to location manager
        """
        self.location_manager.latitude = latitude
        self.location_manager.longitude = longitude
        self.location_manager.altitude = altitude