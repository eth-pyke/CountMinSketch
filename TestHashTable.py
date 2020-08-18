from classes.HashTable import HashTable

def increment(ht:HashTable, key):
    ht.insert(key, ht.find(key) + 1)

if __name__ == '__main__':
    ht = HashTable(26)
    print(ht.size())

    # Insert string representation of numbers 1-26 into the HashTable with
    # a starting value of 0.
    for i in range(26):
        ht.insert(str(i), 0)
    # Verify our table can find every element and print the value that
    # should be 0.
    for i in range(26):
        print("key: " + str(i) + " value: " + str(ht.find(str(i))))

    # Increment and reprint every value.
    for i in range(26):
        increment(ht, str(i))
        print("key: " + str(i) + " value: " + str(ht.find(str(i))))

    # Test find()
    print(ht.find(str(1)) == 1)
    print(ht.find(str(2)) == 1)
    print(ht.find(str(3)) == 1)
    
    # Test size()
    print(ht.size())

    # Test increment()
    increment(ht, str(25))
    print(ht.find(str(25)) == 2)