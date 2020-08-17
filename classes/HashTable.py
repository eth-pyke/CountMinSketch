class HashTable(object):
    def __init__(self, size=32):
        """
        Initialize an array of the given size to store all the key value pairs.

        :param size: The size of the table we want to make.
        """
        self.array = [None] * size
        self.numElements = 0
        self.uniqueSize = 0

    def hash(self, key):
        """
        Hashing function to determine spot in the Table

        :param key: The key to be hashed.
        :return: The resulting index in self.array.
        """
        length = len(self.array)
        return hash(key) % length

    def insert(self, key, value):
        """
        Insert a key value pair into the Hash Table in the form of a 2
        element array.

        :param key: The key to be hashed.
        :param value: The value associated with the key. 
        """
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
                self.uniqueSize += 1
        else:
            self.array[index] = []
            self.array[index].append([key, value])
            self.uniqueSize += 1
            self.numElements += 1

    def find(self, key):
        """
        Given a key, returns the associated value with it.

        :param key: The key whose value we are looking up.
        :return: The associated value of key.
        """
        index = self.hash(key)
        if self.array[index] is None:
            raise KeyError()
        else:
            for pair in self.array[index]:
                if pair[0] == key:
                    return pair[1]
            raise KeyError()

    def size(self):
        """
        Return number of elements within the Hash Table.

        :return: The number of elements in the Hash Table
        """
        return self.uniqueSize

    def is_full(self):
        """
        Determine if the HashTable needs to be resized.
        
        :return: True if full.
        """
        return self.numElements > len(self.array)/2

    def resize(self):
        """
        Doubles size of the array in this HashTable and then
        re-hashes all the elements within this into the newly
        sized array.
        """
        ht = HashTable(len(self.array) * 2)
        for i in range(len(self.array)):
            if self.array[i] is not None:
                for pair in self.array[i]:
                    ht.insert(pair[0], pair[1])
        self.array = ht.array