from classes.HashTable import HashTable

if __name__ == '__main__':
    ht = HashTable()
    print(ht.size())

    ht.insert(1, "TEST")
    print(ht.find(1))