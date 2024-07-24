#!/usr/bin/env python3
""" FIFOCache module
"""

from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    """ FIFOCache defines a caching system with a FIFO eviction policy """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.order = []  # To keep track of the order of keys

    def put(self, key, item):
        """ Assign to the dictionary self.cache_data the item value for the key key """
        if key is not None and item is not None:
            if key not in self.cache_data:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    first_key = self.order.pop(0)
                    del self.cache_data[first_key]
                    print("DISCARD: {}".format(first_key))
            self.cache_data[key] = item
            if key not in self.order:
                self.order.append(key)

    def get(self, key):
        """ Return the value in self.cache_data linked to key """
        return self.cache_data.get(key, None)