from classes.HashTable import HashTable

def increment(ht:HashTable, key):
    ht.insert(key, ht.find(key) + 1)

if __name__ == '__main__':
    ht = HashTable(26)
    print(ht.size())

    for i in range(26):
        ht.insert(str(i), 0)
    for i in range(26):
        print("key: " + str(i) + " value: " + str(ht.find(str(i))))

    for i in range(26):
        increment(ht, str(i))
        print("key: " + str(i) + " value: " + str(ht.find(str(i))))

    print(ht.find(str(1)) == 1)
    print(ht.size())
    increment(ht, str(25))
    print(ht.find(str(25)) == 2)

    for i in range(26):
        print("key: " + str(i) + " value: " + str(ht.find(str(i))))