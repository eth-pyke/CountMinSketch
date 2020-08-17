import numpy as np
import hashlib

class CountMinSketch(object):
    def __init__(self, num_hash, buckets):
        """
        Initialize a [num_hash x buckets] table with all zeroes.

        :param num_hash: The number of hash functions / rows in the table
        :param buckets: The number of buckets that each hash function will hash to
        """
        self.num_hash = num_hash
        self.buckets = buckets
        self.table = np.zeros([num_hash, buckets])
    
    def insert(self, key):
        """
        Inserts an element into the table by incrementing its given hash values at
        each row in the table (according to the hash function at that row).

        :param key: The element to be inserted.
        """
        for i in range(self.num_hash):
            hash_val = self.hash(key, i)
            self.table[i, hash_val] = self.table[i, hash_val] + 1

    def hash(self, key, i):
        """
        Computes the hash value of 'key' according to the i-th hash function in the table.

        :param key: The element to be hashed
        :param i: Indicates which hash function is being used
        :return: Hash value of 'key'
        """
        return int((hash(key) + self.hash2(key) * i)) % self.buckets

    def count(self, key):
        """
        Estimates the number of occurrences of 'key' that we have seen.

        :param key: The element whose count we are estimating
        :return: The estimated total count of 'key'
        """
        min_count = self.table[0, self.hash(key, 0)]
        for i in range(1, self.num_hash):
            min_count = min(min_count, self.table[i, self.hash(key, i)])
        return int(min_count)

    def hash2(self, key):
        """
        Helper function for self.hash()
        """
        return int(hashlib.md5(key.encode('utf-8')).hexdigest()[:8], 16)
