from classes.CountMinSketch import CountMinSketch

if __name__ == '__main__':
    cms = CountMinSketch(5, 10)

    print(cms)

    key1 = "hello"
    key2 = "world"
    key3 = "cse312"

    for i in range(25):
        cms.insert(key1)
        cms.insert(key2)
        cms.insert(key3)

    print("expected: 25")
    print("\"hello\" actual: " + str(cms.count(key1)))
    print("\"world\" actual: " + str(cms.count(key2)))
    print("\"cse312\" actual: " + str(cms.count(key3)))

    for i in range(10):
        cms.insert("ethan")
        cms.insert("david")
        cms.insert("pyke")
        cms.insert("lee")
    
    print("expected: 25")
    print("\"hello\" actual: " + str(cms.count(key1)))
    print("\"world\" actual: " + str(cms.count(key2)))
    print("\"cse312\" actual: " + str(cms.count(key3)))

    print("expected: 10")
    print("\"ethan\" actual: " + str(cms.count("ethan")))
    print("\"david\" actual: " + str(cms.count("david")))
    print("\"pyke\" actual: " + str(cms.count("pyke")))
    print("\"lee\" actual: " + str(cms.count("lee")))

    print("expected: 0")
    print("\"ethan pyke\" actual: " + str(cms.count("ethan pyke")))
    print("\"david lee\" actual: " + str(cms.count("david lee")))