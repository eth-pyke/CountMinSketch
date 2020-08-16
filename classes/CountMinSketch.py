import numpy as np

class CountMinSketch(object):
    def __init__(self, hash, buckets):
        self.hash = hash
        self.buckets = buckets
        self.table = np.zeros([hash, buckets])
    
    def increment(self, key):
        for i in range(self.hash):
            self.table[i, self.hash(key, i)] += 1

    def hash(self, key, i):
        return (hash(key) + i) % self.buckets

    def count(self, key):
        min_count = self.table[0, self.hash(key, 0)]
        for i in range(1, self.hash):
            min_count = min(min_count, self.table[i, self.hash(key, i)])
        return min_count