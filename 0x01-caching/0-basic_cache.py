#!/usr/bin/env python3
""" BasicCache module
"""

from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """ BasicCache defines a caching system with no limit """

    def put(self, key, item):
        """ Assign to the dictionary self.cache_data the item value for the key key """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Return the value in self.cache_data linked to key """
        return self.cache_data.get(key, None)
