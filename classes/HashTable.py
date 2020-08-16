class HashTable(object):
    """
    Initialize an array of the given size to store all the key value pairs.

    :param size: The size of the table we want to make.
    """
    def __init__(self, size=128):
        self.array = [None] * size
        self.numElements = 0

    """
    Hashing function to determine spot in the Table

    :param key: The key to be hashed.
    :return: The resulting index in self.array.
    """
    def hash(self, key):
        length = len(self.array)
        return hash(key) % length

    """
    Insert a key value pair into the Hash Table in the form of a 2
    element array.

    :param key: The key to be hashed.
    :param value: The value associated with the key. 
    """
    def insert(self, key, value):
        index = self.hash(key)
        if (self.array[index] is None):
            self.numElements = self.numElements + 1
        self.array[index] = [key, value]

    """
    Given a key, returns the associated value with it.  If collisions occur,
    could return a value associated with a different key.  If it hashs to the same
    index.

    :param key: The key whose value we are looking up.
    :return: The associated value of key.
    """
    def find(self, key):
        index = self.hash(key)
        if self.array[index] is None:
            raise KeyError()
        else:
            return self.array[index][1]

    """
    Return number of elements within the Hash Table.

    :return: The number of elements in the Hash Table
    """
    def size(self):
        return self.numElements