#!/usr/bin/env python

# increase(7)
# decrease(7)
# increase(8)
# get_most_popular()

class Poppy:
    def __init__(self):
        self.p_id_poppy = defaultdict(int)
        self.inverse = defaultdict(list)   # counting sort buckets
        self.max_poppy = 0
        self.max_poppy_pid = 0

    def increase(self, p_id):
        if p_id not in self.p_id_poppy:        
            self.p_id_poppy[p_id] = 0
            self.inverse[0].append(p_id)
        
        prev_poppy = self.p_id_poppy[p_id]
        self.inverse[prev_poppy].remove(p_id) # LRU
        
        self.p_id_poppy[p_id] = prev_poppy + 1
        self.inverse[prev_poppy + 1].append(p_id)
        
        if prev_poppy == self.max_poppy:
            self.max_poppy += 1
            self.max_poppy_pid = p_id

    def decrease(self):
        prev_poppy = self.p_id_poppy[p_id]
        self.inverse[prev_poppy].remove(p_id) # LRU
        
        self.p_id_poppy[p_id] = prev_poppy + 1
        self.inverse[prev_poppy + 1].append(p_id)
        
        if prev_poppy == self.max_poppy:
            if not self.inverse[prev_poppy]:
                self.max_poppy -= 1
            else:
                self.max_poppy_pid = self.inverse[max_poppy][0]

    def get_poppy(self):
        self.inverse[self.max_poppy][0]


