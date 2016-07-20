from enum import Enum


class PlayerProfile(object):

    def __init__(self):
        self.creation_time = None
        self.username = None
        self.team = None
        self.pokemon_storage = None
        self.item_storage = None
        self.badge = None
        self.avatar = None
        self.daily_bonus = None
        self.contact_settings = None
        self.currencies = None

    def __str__(self):
        return str(self.username)


class Team(Enum):
    TEAM_NONE = 0
    TEAM_MYSTIC = 1
    TEAM_INSTINCT = 2
    TEAM_VALOR = 3


class PlayerAvatar(object):

    def __init__(self):
        self.gender = None
        self.skin = None
        self.hair = None
        self.shirt = None
        self.pants = None
        self.hat = None
        self.shoes = None
        self.eyes = None
        self.backpack = None

    def __str__(self):
        return str(self.skin)


class DailyBonus(object):

    def __init__(self):
        self.next_collection_timestamp = None
        self.next_defender_bonus_collect_timestamp = None
    
    def __str__(self):
        return str(self.next_collection_timestamp)


class ContactSettings(object):

    def __init__(self):
        self.send_marketing_emails = None
        self.send_push_notifications = None
    
    def __str__(self):
        return str(self.send_marketing_emails)