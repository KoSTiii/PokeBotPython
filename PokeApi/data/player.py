import datetime

from PokeApi.data import basedata
from POGOProtos.Data_pb2 import PlayerData


class DataPlayer(basedata.BaseData):
    """
    """

    def __init__(self, api, player_data):
        """
        """
        basedata.BaseData.__init__(self, api, player_data)

    def __str__(self):
        """
        """
        return str(self.data)

    def update(self, plyr=None):
        """
        """
        if plyr:
            self.data = plyr
        else:
            self.api.get_player()
            resp = self.api.send_requests()
            self.data = resp.player_data

    def get_creation_time(self):
        """
        """
        return datetime.datetime.fromtimestamp(
            self.data.creation_timestamp_ms / 1000.0)

    def get_username(self):
        """
        """
        return self.data.username

    def get_team(self):
        """
        """
        return self.data.team

    def get_max_pokemon_storage(self):
        """
        """
        return self.data.max_pokemon_storage

    def get_max_item_storage(self):
        """
        """
        return self.data.max_item_storage

    def get_currencies(self):
        """
        """
        return self.data.currencies

    def get_contact_settings(self):
        """
        """
        return self.data.contact_settings
