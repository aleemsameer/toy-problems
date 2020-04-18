from collections import OrderedDict

class LRUCache():
    def _init_(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()