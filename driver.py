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

"""
This function was taken from matplotlib.org
"""
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

if __name__ == '__main__':
    # Open all the files (sorted from smallest to largest)
    # tiny = open("text/tiny_home-on-the-range.txt", "r")
    cse = "cse312.txt"
    alice = "aliceinwonderland.txt"
    moby = "mobydick.txt"
    monte = "countofmontecristo.txt"
    war = "warandpeace.txt"
    filenames = [cse, alice, moby, monte, war]
    filewordcounts = [170, 29455, 215133, 462169, 565450]

    ntrials = 3

    actual_counts = []
    estimate_counts = []
    for filename in filenames:
        filepath = "text/" + filename
        # insertion
        cms, cms_time = insertCMS(5, 272, filepath)
        ht, ht_time = insertHT(filepath)

        # search
        cms_count, cms_search_time = searchCMS(cms, "the")
        ht_count, ht_search_time = searchHT(ht, "the")

        actual_counts.append(ht_count)
        estimate_counts.append(cms_count)

    x = np.arange(len(filenames))  # the label locations
    width = 0.4  # width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, actual_counts, width, label='Actual')
    rects2 = ax.bar(x + width/2, estimate_counts, width, label='Estimate')

    ax.set_ylabel('Number of occurrences of \"the\"')
    ax.set_xlabel('Number of total words in input file')
    ax.set_xticks(x)
    ax.set_xticklabels(filewordcounts)
    ax.legend()
    autolabel(rects1)
    autolabel(rects2)
    fig.tight_layout()
    fig.savefig('cms_actual_estimate.png')

    # # HT vs CMS Insertion
    # fig, (iplot, splot) = plt.subplots(2,1)
    # for i in range(ntrials):
    #     ht_init_times = []
    #     cms_init_times = []
    #     ht_search_times = []
    #     cms_search_times = []
    #     for filename in filenames:
    #         filepath = "text/" + filename
    #         # insertion time
    #         cms, cms_time = insertCMS(10, 500, filepath)
    #         ht, ht_time = insertHT(filepath)

    #         cms_init_times.append(cms_time)
    #         ht_init_times.append(ht_time)

    #         # search time
    #         cms_count, cms_search_time = searchCMS(cms, "the")
    #         ht_count, ht_search_time = searchHT(ht, "the")

    #         cms_search_times.append(cms_search_time)
    #         ht_search_times.append(ht_search_time)

    #         print("{} has {} distinct words".format(filename, ht.size()))
    #         print("     (HT) actual count \"the\": {}".format(ht_count))
    #         print("     (CMS) estimated count \"the\": {}".format(cms_count))

    #     iplot.plot(filewordcounts, ht_init_times, 'bo', filewordcounts, ht_init_times, 'b--')
    #     iplot.plot(filewordcounts, cms_init_times, 'rs', filewordcounts, cms_init_times, 'r--')

    #     splot.plot(filewordcounts, ht_search_times, 'bo', filewordcounts, ht_search_times, 'b--')
    #     splot.plot(filewordcounts, cms_search_times, 'rs', filewordcounts, cms_search_times, 'r--')

    # iplot.set_ylabel('Insertion Time (seconds)')
    # splot.set_ylabel('Search Time (seconds)')
    # splot.set_xlabel('Number of Words Inserted')
    # fig.suptitle('CMS vs HashTable Time')
    # fig.savefig('cms_ht_time.png', bbox_inches='tight')
    