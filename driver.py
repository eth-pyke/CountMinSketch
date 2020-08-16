from classes.HashTable import HashTable
from classes.CountMinSketch import CountMinSketch

import numpy as np
import matplotlib.pyplot as plt
import timeit

def createCMS(num_hash, buckets, file):
    cms = CountMinSketch(num_hash, buckets)

    for line in file:
        for word in line.split():
            cms.insert(word)

    return cms

def createHT(file):
    ht = HashTable()
    for line in file:
        for word in line.split():
            try:
                ht.insert(word, ht.find(word) + 1)
                break
            except KeyError:
                ht.insert(word, 1)
    return ht

def timeSearchCMS(cms, word):
    pass

def timeSearchHT(ht, word):
    pass

if __name__ == '__main__':
    # Open all the files (sorted from smallest to largest)
    tiny = open("text\\tiny_home-on-the-range.txt", "r")
    cse = open("text\\CSE312.txt", "r")
    alice = open("text\\aliceinwonderland.txt", "r")
    moby = open("text\\mobydick.txt", "r")
    monte = open("text\\countofmontecristo.txt", "r")
    war = open("text\\warandpeace.txt", "r")
    king = open("text\\kingjamesbible.txt", "r")

    start = timeit.timeit()
    tiny_ht = createHT(tiny)
    end = timeit.timeit()
    print("tiny: " + str(end - start))

    start1 = timeit.timeit()
    cse_ht = createHT(cse)
    end1 = timeit.timeit()
    print("cse: " + str(end1 - start1))

    start2 = timeit.timeit()
    alice_ht = createHT(alice)
    end2 = timeit.timeit()
    print("alice: " + str(end2 - start2))

    tiny.close()
    cse.close()
    alice.close()
    moby.close()
    monte.close()
    war.close()
    king.close()