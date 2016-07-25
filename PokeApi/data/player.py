import datetime

import PokeApi.data.basedata as basedata
from POGOProtos.Data_pb2 import PlayerData


class Player(basedata.BaseData):

    def __init__(self, api, player_data):
        basedata.BaseData.__init__(api)
        if not isinstance(player_data, PlayerData):
            raise ValueError('player_data is not type of PlayerData')
        self.player = player_data

    def __str__(self):
        return str(self.player)

    def update_player(self):
        # TODO implement update player
        raise NotImplementedError

    def get_creation_time(self):
        return datetime.datetime.fromtimestamp(
            self.player.creation_timestamp_ms / 1000.0)

    def get_username(self):
        return self.player.username

    def get_team(self):
        return self.player.team

    def get_max_pokemon_storage(self):
        return self.player.max_pokemon_storage

    def get_max_item_storage(self):
        return self.player.max_item_storage

    def get_currencies(self):
        return self.player.currencies

    def get_contact_settings(self):
        return self.player.contact_settings
