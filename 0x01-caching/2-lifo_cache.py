#!/usr/bin/env python3
""" LIFOCache module
"""

from base_caching import BaseCaching # type: ignore

class LIFOCache(BaseCaching):
    """ LIFOCache defines a caching system with a LIFO eviction policy """

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
                last_key = self.order.pop()
                del self.cache_data[last_key]
                print("DISCARD: {}".format(last_key))
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """ Return the value in self.cache_data linked to key """
        return self.cache_data.get(key, None)
