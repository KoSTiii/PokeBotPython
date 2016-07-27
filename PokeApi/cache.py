"""
"""

import os
import json


class Cache(object):
    """
    Cache class for caching
    """
    CACHE_DIR = 'cache/'

    def __init__(self, file_name):
        """
        Initialize cache with file name
        """
        self.file_name = file_name
        self.cache = dict()

    def cache_initialize(self):
        if not os.path.exists(Cache.CACHE_DIR):
            os.makedirs(Cache.CACHE_DIR)
        # if file does not exists we create it
        with open(self.CACHE_DIR + self.file_name, 'a'):    
            pass

        try:
            self.load()
        except:
            pass

    def cache_reset(self):
        """
        reset cache
        """
        self.cache = dict()

    def get_cache(self, key):
        """
        return cache entry for key
        if key not exists then raise exception
        """
        if not self.cache[key]:
            raise KeyError
        return self.cache[key]
    
    def add_cache(self, key, value):
        """
        add new cache entry
        if key exists then raise exception
        """
        if self.cache[key]:
            raise KeyError
        self.cache[key] = value

    def update(self, key, value):
        """
        update cache value for new one
        """
        if not self.cache[key]:
            raise KeyError
        self.cache[key] = value

    def get_all_keys(self):
        """
        return all keys stored in cache
        """
        return self.cache.keys()
        
    def get_all_values(self):
        """
        return all values in array
        """
        return self.cache.values()

    def save(self):
        """
        save cache on disk
        """
        with open(self.CACHE_DIR + self.file_name, 'w') as outfile:
            json.dump(self.cache, outfile)

    def load(self):
        """
        load cache from disk
        """
        with open(self.CACHE_DIR + self.file_name, 'r') as data_file:    
            self.cache = json.load(data_file)
        

    