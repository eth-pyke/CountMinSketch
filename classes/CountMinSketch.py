import numpy as np
import hashlib

class CountMinSketch(object):
    def __init__(self, num_hash, buckets):
        self.num_hash = num_hash
        self.buckets = buckets
        self.table = np.zeros([num_hash, buckets])
    
    def insert(self, key):
        for i in range(self.num_hash):
            hash_val = self.hash(key, i)
            self.table[i, hash_val] = self.table[i, hash_val] + 1

    def hash(self, key, i):
        return (hash(key) + self.hash2(key) * i) % self.buckets

    def count(self, key):
        min_count = self.table[0, self.hash(key, 0)]
        for i in range(1, self.num_hash):
            min_count = min(min_count, self.table[i, self.hash(key, i)])
        return min_count

    def hash2(self, key):
        return int(hashlib.md5(key.encode('utf-8')).hexdigest()[:8], 16)
