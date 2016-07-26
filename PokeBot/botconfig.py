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
    if pokemon_name.upper() in Enums_pb2.PokemonType.keys():
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
    def from_file(cls, json_file):
        """ Initialize BotConfigs from json file
        """
        configs = []
        fjson = json.load(open(json_file))

        # make bot configs objects
        for cfg in fjson:
            if not cfg['active']:
                continue
            pokemon_release_configs = []
            for rel_pok in cfg['release_pokemon']:
                pokemon_release_configs.append(PokemonReleaseConfig.from_json(rel_pok, cfg['release_pokemon']))

            config = cls(cfg['provider'],
                         cfg['username'],
                         cfg['password'],
                         cfg['location'],
                         cfg['mode'],
                         cfg['cache'],
                         cfg['maxsteps'],
                         cfg['steps'],
                         cfg['ignore_pokemon'],
                         pokemon_release_configs,
                         cfg['items_filter'])
        return configs
            configs.append(config)  

    def __init__(self, provider, username, password, location, mode, cache, maxsteps, steps, ignore_pokemon, release_pokemon, items_filter):
        """ Initialize bot config
        """
        self.provider = self._check_providers(provider)
        self.username = username
        self.password = password
        self.location = location
        self.mode = self._check_mode(mode)
        self.cache = cache
        self.maxsteps = maxsteps
        self.steps = steps
        self.ignore_pokemon = self._check_ignore_pokemon(ignore_pokemon)
        self.release_pokemon = self._check_release_pokemon(release_pokemon)
        self.items_filter = self._check_items_filter(items_filter)

    def _check_providers(self, provider):
        if provider not in SUPPORTED_PROVIDERS:
            raise ValueError('Provider {} is not supported.'.format(provider))
        return provider

    def _check_mode(self, mode):
        if mode not in SUPPORTED_MODES:
            raise ValueError('Mode {} is not supported.'.format(mode))
        return mode

    def _check_ignore_pokemon(self, ignore_pokemon):
        for pokemon in ignore_pokemon:
            if not check_pokemon_name(pokemon):
                raise ValueError('Unknown pokemon {}'.format(pokemon))
        return ignore_pokemon

    def _check_release_pokemon(self, release_pokemon):
        for rel_pok in release_pokemon:
            if not isinstance(rel_pok, PokemonReleaseConfig):
                raise TypeError('release_pokemon array element is not instance of PokemonReleaseConfig.')
        return release_pokemon

    def _check_items_filter(self, items_filter):
        for item in items_filter:
            if not check_item_id(item):
                raise ValueError('Item with id {} is not valid'.format(item))
        return items_filter
    
    def get_location_manager(self):
        """ Return location in LocationManager class
        """
        coords = self.location.split(',')
        return LocationManager(float(coords[0]), float(coords[1]))


class PokemonReleaseConfig(object):
    """ configuration for pokemon release
    """

    @classmethod
    def from_json(cls, name, json_):
        """
        """
        return cls(name, json_[name]['release_under_cp'], json_[name]['release_under_iv'], json_[name]['cp_iv_logic'])

    def __init__(self, name, release_under_cp, release_under_iv, cp_iv_logic):
        self.name = self._check_name(name)
        self.release_under_cp = release_under_cp
        self.release_under_iv = self._check_release_under_iv(release_under_iv)
        self.cp_iv_logic = self._check_cp_iv_logic(cp_iv_logic)

    def _check_name(self, name):
        if (not check_pokemon_name(name)) and (name is 'any'):
            raise ValueError('Unknown pokemon name or not "any". get: {}'.format(name))
        return name

    def _check_release_under_iv(self, release_under_iv):
        if release_under_iv < 0.0 or release_under_iv > 1.0:
            raise ValueError('release_under_iv must be procent betwen 0.0 and 1.0')
        return release_under_iv

    def _check_cp_iv_logic(self, cp_iv_logic):
        if cp_iv_logic not in SUPPORTED_CP_IV_LOGIC:
            raise ValueError('CP IV logic get unsoported operation of {}'.format(cp_iv_logic)) 
        return cp_iv_logic
