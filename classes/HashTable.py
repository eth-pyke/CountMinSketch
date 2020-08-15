class HashTable(object):
    def __init__(self, size=128):
        self.array = [None] * size

    def hash(self, key):
        length = len(self.array)
        return hash(key) % length

    def insert(self, key, value):
        index = self.hash(key)
        self.array[index] = [key, value]

    def find(self, key):
        index = self.hash(key)
        if self.array[index] is None:
            raise KeyError()
        else:
            return self.array[index][1]

    def size(self):
        return len(self.array)

    def increment(self, key):
        index = self.hash(key)
        self.array[index][1] = self.array[index][1] + 1