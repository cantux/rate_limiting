from collections import OrderedDict
class LRU:
    def __init__(self, capacity):
        self.capacity = capacity
        self.store = OrderedDict()

    def put(self, key, value):
        if key not in self.store:
            if len(self.store) == self.capacity:
                self.store.popitem(last=False)
        else:
            self.store.move_to_end(key)
        self.store[key] = value

    def get(self, key):
        if key not in self.store:
            res = -1
        else:
            self.store.move_to_end(key)
            res = self.store[key]
        return res