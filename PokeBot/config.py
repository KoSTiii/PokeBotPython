import json

from PokeApi.locations import LocationManager

# BotConfig settings
SUPPORTED_PROVIDERS = ['ptc', 'google']
SUPPORTED_MODES = ['all', 'pokemon', 'pokestop']

# ReleasePokemonConfig settings
SUPPORTED_CP_IV_LOGIC = ['or', 'and']

# Pokemon and Items data
SUPPORTED_POKEMONS = []
SUPPORTED_ITEMS = []

def init_pokemon_and_item_data():
    if not SUPPORTED_POKEMONS: 
        global SUPPORTED_POKEMONS
        SUPPORTED_POKEMONS = json.load(open('data/pokemon.json'))
    if not SUPPORTED_ITEMS:
        global SUPPORTED_ITEMS
        SUPPORTED_ITEMS = json.load(open('data/items.json'))
init_pokemon_and_item_data()


""" BotConfig is configuration for bot
"""
class BotConfig(object):

    """ Initialize BotConfigs from json file
    """
    @classmethod
    def from_file(cls, json_file):
        configs = []
        fjson = json.load(open(json_file))

        # make bot configs objects
        for cfg in fjson:
            if not cfg['active']:
                continue
            pokemon_release_configs = []
            for rel_pok in cfg['release_pokemon']:
                pokemon_release_configs.append(PokemonReleaseConfig.from_json(rel_pok))

            config = cls(cfg['provider'],
                         cfg['username'],
                         cfg['password'],
                         cfg['location'],
                         cfg['mode'],
                         cfg['cache'],
                         cfg['maxstep'],
                         cfg['step'],
                         cfg['ignore_pokemon'],
                         pokemon_release_configs,
                         cfg['items_filter'])
            configs.append(config)

        return configs

    """ Initialize bot config
    """
    def __init__(self, provider, username, password, location, mode, cache, maxstep, step, ignore_pokemon, release_pokemon, items_filter):
        self.provider = self._check_providers(provider)
        self.username = username
        self.password = password
        self.location = location
        self.mode = self._check_mode(mode)
        self.cache = cache
        self.maxsteps = maxstep
        self.step = step
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
            if pokemon not in SUPPORTED_POKEMONS:
                raise ValueError('Unknown pokemon {}'.format(pokemon))
        return ignore_pokemon

    def _check_release_pokemon(self, release_pokemon):
        for rel_pok in release_pokemon:
            if not isinstance(rel_pok, PokemonReleaseConfig):
                raise TypeError('release_pokemon array element is not instance of PokemonReleaseConfig.')
        return release_pokemon

    def _check_items_filter(self, items_filter):
        for item in items_filter:
            if item not in SUPPORTED_ITEMS:
                raise ValueError('Item with id {} is not valid'.format(item))
        return items_filter
    
    """ Return location in LocationManager class
    """
    def get_location_manager(self):
        coords = self.location.split(',')
        return LocationManager(float(coords[0]), float(coords[1]))


""" configuration for pokemon release
"""
class PokemonReleaseConfig(object):

    """
    """
    @classmethod
    def from_json(cls, json_):
        return cls(json_, json_['release_under_cp'], json_['release_under_iv'], json_['cp_iv_logic'])

    def __init__(self, name, release_under_cp, release_under_iv, cp_iv_logic):
        self.name = self._check_name(name)
        self.release_under_cp = release_under_cp
        self.release_under_iv = self._check_release_under_iv(release_under_iv)
        self.cp_iv_logic = self._check_cp_iv_logic(cp_iv_logic)

    def _check_name(self, name):
        if name is not 'any' and name not in SUPPORTED_POKEMONS:
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
