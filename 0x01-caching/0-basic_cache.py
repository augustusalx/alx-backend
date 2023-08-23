#!/usr/bin/env python3
""" The baseCaching module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Defines a class for caching information in key-value pairs
    """

    def __init__(self):
        """
        Initializing the class using parent class _init_ method
        """
        BaseCaching.__init__(self)

    def put(self, key, item):
        """
        To store this key-value pair
        Args:
            Key
            Item
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Return value linked to key.
        Return None if key doesn't exist
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
