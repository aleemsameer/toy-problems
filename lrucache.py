from collections import OrderedDict

class LRUCache():
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()
    
    def put(self, key, value):
        pass
        if self.get(key) == -1:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last = False)
        self.cache[key] = value
    
    def get(self, key):
        pass
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1
    
    def get_cache(self):
        pass
        return self.cache
