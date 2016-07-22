from PokeApi import exceptions, mapobjects
from PokeApi.auth import PTCLogin, Auth
from PokeApi.requesthandler import RequestHandler
from PokeApi.serverrequest import ServerRequest
from PokeApi.auth import Auth
from PokeApi.locations import LocationManager
from POGOProtos.Networking.Envelopes_pb2 import AuthTicket, ResponseEnvelope, RequestEnvelope, Unknown6
from POGOProtos.Networking import Requests_pb2
from POGOProtos.Networking.Requests import Messages_pb2
#data imports
from PokeApi.data.player import *

import s2sphere


class PokeApi(object):

    """
    """
    def __init__(self, auth, location):
        self.auth = auth
        self.request_handler = RequestHandler(auth)
        self.location_manager = location

        self.request_handler.set_location(self.location_manager)

    def get_profile(self):
        player = ServerRequest(Requests_pb2.GET_PLAYER)
        inv = ServerRequest(Requests_pb2.GET_INVENTORY)
        eggs = ServerRequest(Requests_pb2.GET_HATCHED_EGGS)
        settMessage = Messages_pb2.DownloadSettingsMessage()
        settMessage.hash = '05daf51635c82611d1aac95c0b051d3ec088a930'
        sett = ServerRequest(Requests_pb2.DOWNLOAD_SETTINGS) #, settMessage)
        badges = ServerRequest(Requests_pb2.CHECK_AWARDED_BADGES)
        
        self.request_handler.add_request(player)
        self.request_handler.add_request(inv)
        self.request_handler.add_request(eggs)
        self.request_handler.add_request(sett)
        self.request_handler.add_request(badges)
        self.request_handler.send_requests()

        return [player.get_structured_data(), inv.get_structured_data(), eggs.get_structured_data(), sett.get_structured_data(), badges.get_structured_data()]
    
    def get_settings(self):
        settMessage = Messages_pb2.DownloadSettingsMessage()
        settMessage.hash = '05daf51635c82611d1aac95c0b051d3ec088a930'
        sett = ServerRequest(Requests_pb2.DOWNLOAD_SETTINGS)
        self.request_handler.add_request(sett)
        self.request_handler.send_requests()

        return sett.get_structured_data()

    def get_player(self):
        playerReq = ServerRequest(Requests_pb2.GET_PLAYER)
        self.request_handler.add_request(playerReq)
        self.request_handler.send_requests()

        response = playerReq.get_structured_data()
        """
        player = PlayerProfile()
        player.creation_time = response.creation_timestamp_ms
        player.username = response.username
        player.team = Team.TEAM_NONE
        player.pokemon_storage = response.max_pokemon_storage
        player.item_storage = response.max_item_storage
        player.badge = response.equipped_badge
        player.avatar = response.avatar
        player.daily_bonus = response.daily_bonus
        player.contact_settings = response.contact_settings
        player.currencies = response.currencies
        """
        return response

    def get_inventory(self):
        inv = ServerRequest(Requests_pb2.GET_INVENTORY)
        self.request_handler.add_request(inv)
        self.request_handler.send_requests()

        return inv.get_structured_data()

    def get_map_objects(self):
        map_cells = mapobjects.get_map_objects(self.request_handler, self.location_manager)
        return map_cells
