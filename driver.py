from classes.HashTable import HashTable
from classes.CountMinSketch import CountMinSketch
from timeit import default_timer as timer

import numpy as np
import matplotlib.pyplot as plt

"""
returns 
"""
def insertCMS(num_hash, buckets, filepath):
    file = open(filepath, "r")
    start = timer()

    cms = CountMinSketch(num_hash, buckets)

    for line in file:
        for word in line.split():
            cms.insert(word)

    end = timer()
    file.close()
    time = end - start
    return cms, time

def insertHT(filepath):
    file = open(filepath, "r")
    start = timer()
    
    ht = HashTable()

    for line in file:
        for word in line.split():
            try:
                ht.insert(word, ht.find(word) + 1)
                continue
            except KeyError:
                ht.insert(word, 1)

    end = timer()
    file.close()
    time = end - start
    return ht, time

def searchCMS(cms, word):
    start = timer()
    count = cms.count(word)
    end = timer()
    time = end - start
    return count, time

def searchHT(ht, word):
    start = timer()
    count = ht.find(word)
    end = timer()
    time = end - start
    return count, time

if __name__ == '__main__':
    # Open all the files (sorted from smallest to largest)
    # tiny = open("text/tiny_home-on-the-range.txt", "r")
    tiny = "tiny.txt"
    cse = "cse312.txt"
    alice = "aliceinwonderland.txt"
    moby = "mobydick.txt"
    monte = "countofmontecristo.txt"
    war = "warandpeace.txt"
    bible = "kingjamesbible.txt"
    filenames = [tiny, cse, alice, moby, monte]
    filewordcounts = [9, 170, 29455, 215133, 462169, 565450, 824146]

    # HT vs (10x10)CMS
    ht_init_times = []
    cms10x10_init_times = []
    ht_search_times = []
    cms10x10_search_times = []
    for filename in filenames:
        filepath = "text/" + filename
        # insertion time
        cms, cms_time = insertCMS(10, 100, filepath)
        ht, ht_time = insertHT(filepath)

        cms10x10_init_times.append(cms_time)
        ht_init_times.append(ht_time)

        # search time
        cms_count, cms_search_time = searchCMS(cms, "the")
        ht_count, ht_search_time = searchHT(ht, "the")

        cms10x10_search_times.append(cms_search_time)
        ht_search_times.append(ht_search_time)

        print("{} has {} distinct words".format(filename, ht.size()))
        print("     (HT) actual count \"the\": {}".format(ht_count))
        print("     (CMS) estimated count \"the\": {}".format(cms_count))
