#!/usr/bin/env python3
""" LFUCache module
"""

from base_caching import BaseCaching # type: ignore
from collections import defaultdict, deque

class LFUCache(BaseCaching):
    """ LFUCache defines a caching system with an LFU eviction policy """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.cache_data = {}
        self.frequency = defaultdict(int)  # Frequency of access
        self.order = defaultdict(deque)    # Order of access for items with the same frequency

    def put(self, key, item):
        """ Assign to the dictionary self.cache_data the item value for the key key """
        if key is None or item is None:
            return
        
        if key in self.cache_data:
            # Update item and frequency
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.order[self.frequency[key]].remove(key)
            self.order[self.frequency[key]].append(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Determine the LFU item to discard
                min_freq = min(self.frequency.values())
                lfu_keys = self.order[min_freq]
                key_to_discard = lfu_keys.popleft()
                del self.cache_data[key_to_discard]
                del self.frequency[key_to_discard]
                print("DISCARD: {}".format(key_to_discard))
                if not lfu_keys:
                    del self.order[min_freq]
            
            self.cache_data[key] = item
            self.frequency[key] = 1
            self.order[1].append(key)

    def get(self, key):
        """ Return the value in self.cache_data linked to key """
        if key is None or key not in self.cache_data:
            return None
        
        # Update frequency and order
        freq = self.frequency[key]
        self.order[freq].remove(key)
        if not self.order[freq]:
            del self.order[freq]
        self.frequency[key] += 1
        self.order[self.frequency[key]].append(key)
        
        return self.cache_data[key]
