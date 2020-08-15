from classes.HashTable import HashTable

if __name__ == '__main__':
    ht = HashTable(26)
    print(ht.size())

    for i in range(26):
        ht.insert(i, 0)
    for i in range(26):
        print("key: " + str(i) + " value: " + str(ht.find(i)))

    for i in range(26):
        ht.increment(i)
        print("key: " + str(i) + " value: " + str(ht.find(i)))

    print(1 == ht.find(1))
