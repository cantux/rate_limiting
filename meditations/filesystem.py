
#!/usr/bin/env python

# ask what happens for tie break
# get top N collections by filesize
# recursive
# doing lazy vs greedy calc

from collections import defaultdict
import heapq

class Filesystem:
    def __init__(self):
        self.coll_size = defaultdict(int)

    def set_files(file_list, k):
        coll_size = self.coll_size
        for filename, size, coll in file_list:
            coll_size[coll] += size

        h = []
        coll_size_list = [(v, k) for k, v in coll_size.items()]
        len_csl = len(coll_size_list)
        for i in range(k):
            heapq.heappush(h, coll_size_list[i])
        
        for i in range(k, len_csl):
            curr = coll_size_list[i]
            if h[0][0] < curr[0]:
                heapq.heappop(h)
                heapq.heappush(h, curr)
        return h


class RecFilesystem:
    def __init__(self):
        self.g = defaultdict(list)
        coll_size = defaultdict(int)
        
    def set_files(self, file_list, rel_pairs):
        for parent, child in rel_pairs:
            self.g[parent].append(child)

        for coll, size in file_list:
            coll_size[coll] += size

        seen = set()
        for k, children in self.g.items():
            if k not in seen:
                update_coll_size(k)

        def update_coll_size(curr):
            seen.add(curr)
            if curr not in self.g:
                return self.coll_size[curr]

            children_size = 0
            for child in g[curr]:
                children_size += update_coll_size(child)

            self.coll_size[curr] += children_size

class StreamFilesystem:
    def __init__(self):
        self.coll_size = defaultdict(int)
        self.parent_rel = {}

    def create_directory(dir_name, parent_name):
        self.parent_rel[dir_name] = parent_name

    def create_file(coll, size):
        curr = coll
        c_size = size
        while curr in self.parent_rel:
            self.coll_size[curr] += size
            curr = self.parent_rel[curr]
    
    def get_coll_size(self, coll):
        return self.coll_size[coll]
