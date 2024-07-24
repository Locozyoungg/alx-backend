#!/usr/bin/env python3
""" LRUCache module
"""

from base_caching import BaseCaching # type: ignore
from collections import OrderedDict

class LRUCache(BaseCaching):
    """ LRUCache defines a caching system with an LRU eviction policy """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Assign to the dictionary self.cache_data the item value for the key key """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data.move_to_end(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_key, _ = self.cache_data.popitem(last=False)
                print("DISCARD: {}".format(lru_key))
            self.cache_data[key] = item

    def get(self, key):
        """ Return the value in self.cache_data linked to key """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None
