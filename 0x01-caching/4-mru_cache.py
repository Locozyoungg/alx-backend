#!/usr/bin/env python3
""" MRUCache module
"""

from base_caching import BaseCaching # type: ignore

class MRUCache(BaseCaching):
    """ MRUCache defines a caching system with an MRU eviction policy """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.order = []  # To keep track of the order of keys

    def put(self, key, item):
        """ Assign to the dictionary self.cache_data the item value for the key key """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                mru_key = self.order.pop()  # Most recently used key
                del self.cache_data[mru_key]
                print("DISCARD: {}".format(mru_key))
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """ Return the value in self.cache_data linked to key """
        if key is not None and key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None
