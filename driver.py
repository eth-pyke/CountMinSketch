from classes.HashTable import HashTable
from classes.CountMinSketch import CountMinSketch

import numpy as np
import matplotlib.pyplot as plt
import timeit

def createCMS(file):
    pass

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

if __name__ == '__main__':
    # Open all the files (sorted from smallest to largest)
    tiny = open("text\\tiny_home-on-the-range.txt", "r")
    cse = open("text\\CSE312.txt", "r")
    alice = open("text\\aliceinwonderland.txt", "r")
    moby = open("text\\mobydick.txt", "r")
    monte = open("text\\countofmontecristo.txt", "r")
    war = open("text\\warandpeace.txt", "r")
    king = open("text\\kingjamesbible.txt", "r")

    tiny.close()
    cse.close()
    alice.close()
    moby.close()
    monte.close()
    war.close()
    king.close()