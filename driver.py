from classes.HashTable import HashTable
from classes.CountMinSketch import CountMinSketch
from timeit import default_timer as timer

import numpy as np
import matplotlib.pyplot as plt

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
                continue
            except KeyError:
                ht.insert(word, 1)
                
    return ht

def timeSearchCMS(cms, word):
    pass

def timeSearchHT(ht, word):
    start = timer()
    print(ht.find(word))
    end = timer()
    return end - start

if __name__ == '__main__':
    # Open all the files (sorted from smallest to largest)
    tiny = open("text/tiny_home-on-the-range.txt", "r")
    cse = open("text/CSE312.txt", "r")
    alice = open("text/aliceinwonderland.txt", "r")
    moby = open("text/mobydick.txt", "r")
    monte = open("text/countofmontecristo.txt", "r")
    war = open("text/warandpeace.txt", "r")
    king = open("text/kingjamesbible.txt", "r")

    start = timer()
    tiny_ht = createHT(tiny)
    end = timer()
    print("tiny: " + str(end - start))

    start = timer()
    cse_ht = createHT(cse)
    end = timer()
    print("cse: " + str(end - start))

    start = timer()
    alice_ht = createHT(alice)
    end = timer()
    print("alice: " + str(end - start))

    start = timer()
    moby_ht = createHT(moby)
    end = timer()
    print("moby: " + str(end - start))

    tiny.close()
    cse.close()
    alice.close()
    moby.close()
    monte.close()
    war.close()
    king.close()