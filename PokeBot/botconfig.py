import json

import POGOProtos.Enums_pb2 as Enums_pb2
import POGOProtos.Inventory_pb2 as Inventory_pb2
from PokeApi.locations import LocationManager

# BotConfig settings
SUPPORTED_PROVIDERS = ['ptc', 'google']
SUPPORTED_MODES = ['all', 'pokemon', 'pokestop']

# ReleasePokemonConfig settings
SUPPORTED_CP_IV_LOGIC = ['or', 'and']

def check_pokemon_name(pokemon_name):
    if pokemon_name.upper() in Enums_pb2.PokemonId.keys():
        return True
    return False

def check_item_id(item_id):
    if item_id in Inventory_pb2.ItemId.values():
        return True
    return False


class BotConfig(object):
    """ BotConfig is configuration for bot
    """

    @classmethod
    def from_file(cls, json_file, item_cfg=None, poke_cfg=None):
        """ Initialize BotConfigs from json file
        """
        configs = []
        fjson = json.load(open(json_file))

        # make bot configs objects
        for cfg in fjson:
            if not cfg['active']:
                continue

            config = cls()
            config.provider = BotConfig.check_providers(cfg['provider'])
            config.username = cfg['username']
            config.password = cfg['password']
            config.location = cfg['location']
            config.mode = BotConfig.check_mode(cfg['mode'])
            config.cache = cfg['cache']
            config.maxsteps = cfg['maxsteps']
            config.steps = cfg['steps']

            config.pokemon_config = poke_cfg
            config.item_config = item_cfg
            configs.append(config)

        return configs

    def __init__(self):
        """ Initialize bot config
        """
        self.provider = None
        self.username = None
        self.password = None
        self.location = None
        self.mode = None
        self.cache = None
        self.maxsteps = None
        self.steps = None

        self.pokemon_config = None
        self.item_config = None
    
    def to_JSON(self):
        """
        convert class to json
        """
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def get_location_manager(self):
        """ Return location in LocationManager class
        """
        coords = self.location.split(',')
        return LocationManager(float(coords[0]), float(coords[1]))

    @classmethod
    def check_providers(cls, provider):
        if provider not in SUPPORTED_PROVIDERS:
            raise ValueError('Provider %s is not supported.', provider)
        return provider

    @classmethod
    def check_mode(cls, mode):
        if mode not in SUPPORTED_MODES:
            raise ValueError('Mode %s is not supported.', mode)
        return mode


class ItemsConfig(object):
    """
    """

    @classmethod
    def from_json(cls, json_file):
        fjson = json.load(open(json_file))

        items_cfg = cls()
        
        for item in fjson['items']:
            item_cfg = ItemsConfig.ItemConfig()
            if check_item_id(item['item_id']):
                item_cfg.item_id = item['item_id']
                item_cfg.min_keep_items = item['min_keep_items'] or None
                items_cfg.items.append(item_cfg)
            else:
                raise ValueError
        return items_cfg

    def __init__(self):
        self.items = []


    class ItemConfig(object):

        def __init__(self):
            self.item_id = None
            self.min_keep_items = None


class PokemonConfig(object):
    """ configuration for pokemon release
    """

    @classmethod
    def from_json(cls, json_file):
        fjson = json.load(open(json_file))

        pokemons_cfg = cls()
        pokemons_cfg.ignore_pokemon = [pok for pok in fjson['ignore_pokemon'] if check_pokemon_name(pok['name'])]

        for rel_pok_json in fjson['release_pokemon']:
            rel_pok = PokemonConfig.PokemonReleaseConfig()
            rel_pok.name = PokemonConfig.PokemonReleaseConfig.check_name(rel_pok_json['name'])
            rel_pok.release_under_cp = rel_pok_json['release_under_cp']
            rel_pok.release_under_iv = PokemonConfig.PokemonReleaseConfig.check_release_under_iv(rel_pok_json['release_under_iv'])
            rel_pok.cp_iv_logic = PokemonConfig.PokemonReleaseConfig.check_cp_iv_logic(rel_pok_json['cp_iv_logic'])
            pokemons_cfg.release_pokemon.append(rel_pok)

        return pokemons_cfg

    def __init__(self):
        self.ignore_pokemon = []
        self.release_pokemon = []

    def get_any_config(self):
        any_config = [rpok for rpok in self.release_pokemon if rpok.name.lower() == 'any']

        for conf in any_config:
            return conf
        return None

    def get_pokemon_config(self, pokemon_name):
        """
        return specific pokemon config if found
        else return any config
        """
        poke_conf = [rpok for rpok in self.release_pokemon if rpok.name.upper() == pokemon_name.upper()]
        for conf in poke_conf:
            return conf
        return self.get_any_config()

    class PokemonReleaseConfig(object):
        """
        """

        def __init__(self):
            self.name = None
            self.release_under_cp = None
            self.release_under_iv = None
            self.cp_iv_logic = None

        def get_pokemon_id(self):
            return Enums_pb2.PokemonType.Value(self.name)

        def get_logic_function(self):
            if self.cp_iv_logic == 'or':
                return lambda x, y: x or y
            elif self.cp_iv_logic == 'and':
                return lambda x, y: x and y
            else:
                return None

        @classmethod
        def check_name(cls, name):
            if not (check_pokemon_name(name) or name == 'any'):
                raise ValueError('Unknown pokemon name or not "any". get: %s' % name)
            return name

        @classmethod
        def check_release_under_iv(cls, release_under_iv):
            if release_under_iv < 0.0 or release_under_iv > 1.0:
                raise ValueError('release_under_iv must be procent betwen 0.0 and 1.0')
            return release_under_iv

        @classmethod
        def check_cp_iv_logic(cls, cp_iv_logic):
            if cp_iv_logic not in SUPPORTED_CP_IV_LOGIC:
                raise ValueError('CP IV logic get unsoported operation of %s' % cp_iv_logic)
            return cp_iv_logic



    