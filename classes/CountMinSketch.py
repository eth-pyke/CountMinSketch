import numpy as np
import hashlib

class CountMinSketch(object):
    """
    Initialize a [num_hash x buckets] table with all zeroes.

    :param num_hash: The number of hash functions / rows in the table
    :param buckets: The number of buckets that each hash function will hash to
    """
    def __init__(self, num_hash, buckets):
        self.num_hash = num_hash
        self.buckets = buckets
        self.table = np.zeros([num_hash, buckets])
    
    """
    Inserts an element into the table by incrementing its given hash values at
    each row in the table (according to the hash function at that row).

    :param key: The element to be inserted.
    """
    def insert(self, key):
        for i in range(self.num_hash):
            hash_val = self.hash(key, i)
            self.table[i, hash_val] = self.table[i, hash_val] + 1

    def hash(self, key, i):
        return int((hash(key) + self.hash2(key) * i)) % self.buckets

    def count(self, key):
        min_count = self.table[0, self.hash(key, 0)]
        for i in range(1, self.num_hash):
            min_count = min(min_count, self.table[i, self.hash(key, i)])
        return int(min_count)

    def hash2(self, key):
        return int(hashlib.md5(key.encode('utf-8')).hexdigest()[:8], 16)
