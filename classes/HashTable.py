class HashTable(object):
    """
    Initialize an array of the given size to store all the key value pairs.

    :param size: The size of the table we want to make.
    """
    def __init__(self, size=32):
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

        if self.is_full():
            self.resize()

        # If values have already been hashed to this index
        if self.array[index] is not None:
            # Check list to see if pair is there
            for pair in self.array[index]:
                if pair[0] == key:
                    pair[1] = value
                    break
            else:
                self.array[index].append([key, value])
                self.numElements = self.numElements + 1
        else:
            self.array[index] = []
            self.array[index].append([key, value])
            self.numElements = self.numElements + 1

    """
    Given a key, returns the associated value with it.

    :param key: The key whose value we are looking up.
    :return: The associated value of key.
    """
    def find(self, key):
        index = self.hash(key)
        if self.array[index] is None:
            raise KeyError()
        else:
            for pair in self.array[index]:
                if pair[0] == key:
                    return pair[1]
            raise KeyError()

    """
    Return number of elements within the Hash Table.

    :return: The number of elements in the Hash Table
    """
    def size(self):
        return self.numElements

    def __setitem__(self, key, value):
        self.insert(key, value)

    def __getitem__(self, key):
        return self.find(key)

    def is_full(self):
        return self.numElements > len(self.array)/2

    def resize(self):
        ht = HashTable(len(self.array) * 2)
        for i in range(len(self.array)):
            if self.array[i] is None:
                continue
            for pair in self.array[i]:
                ht.insert(pair[0], pair[1])
        self.array = ht.array