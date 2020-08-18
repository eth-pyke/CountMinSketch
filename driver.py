from classes.HashTable import HashTable
from classes.CountMinSketch import CountMinSketch
from timeit import default_timer as timer

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import re

def insertCMS(num_hash, buckets, filepath):
    """
    Helper function that inputs every word from a file into a CMS and times
    how long the insertion takes.

    :param num_hash: The number of hash functions to use.
    :param buckets: The number of buckets to initialize the CMS with.
    :param filepath: The path to file that we want counted.
    :return: A tuple in the form of (CMS, time)
    """
    file = open(filepath, "r")
    start = timer()

    cms = CountMinSketch(num_hash, buckets)

    for line in file:
        for word in line.split():
            word = re.sub(r'[^\w\s]', '', word)
            cms.insert(word)

    end = timer()
    file.close()
    time = end - start
    return cms, time

def insertHT(filepath):
    """
    Helper function that inputs every word from a file into a Hash Table
    and times how long the insertion takes.

    :param filepath: The path to file that we want counted.
    :return: A tuple in the form of (HT, time)
    """
    file = open(filepath, "r")
    start = timer()
    
    ht = HashTable()

    for line in file:
        for word in line.split():
            word = re.sub(r'[^\w\s]', '', word)
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
    """
    A helper function that returns the frequency of a word within a CMS
    and how long the CMS took to search for it.

    :param cms: Count-Min Sketch to search in.
    :word: A word that we want to search for.
    :return: A tuple in the form of (Frequency, Time)
    """
    start = timer()
    count = cms.count(word)
    end = timer()
    time = end - start
    return count, time

def searchHT(ht, word):
    """
    A helper function that returns the frequency of a word within a Hash Table
    and how long the Hash Table took to search for it.

    :param ht: Hash Table to search in.
    :word: A word that we want to search for.
    :return: A tuple in the form of (Frequency, Time)
    """
    start = timer()
    count = ht.find(word)
    end = timer()
    time = end - start
    return count, time

def autolabel(rects):
    """
    This function was taken from matplotlib.org
    """
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

if __name__ == '__main__':
    # Open all the files (sorted from smallest to largest)
    cse = "cse312.txt"
    alice = "aliceinwonderland.txt"
    moby = "mobydick.txt"
    monte = "countofmontecristo.txt"
    war = "warandpeace.txt"
    filenames = [cse, alice, moby, monte, war]
    filewordcounts = [170, 29455, 215133, 462169, 565450]

    ntrials = 3

    # HT vs CMS Insertion & Search
    fig1, (iplot, splot) = plt.subplots(2,1)
    actual_counts = []
    estimate_counts = []
    unique_counts = []
    for i in range(ntrials):
        ht_init_times = []
        cms_init_times = []
        ht_search_times = []
        cms_search_times = []
        actual_counts_sub = []
        estimate_counts_sub = []
        unique_counts_sub = []
        for filename in filenames:
            filepath = "text/" + filename
            # insertion time
            cms, cms_time = insertCMS(5, 272, filepath)
            ht, ht_time = insertHT(filepath)

            cms_init_times.append(cms_time)
            ht_init_times.append(ht_time)

            # search time
            cms_count, cms_search_time = searchCMS(cms, "the")
            ht_count, ht_search_time = searchHT(ht, "the")

            cms_search_times.append(cms_search_time)
            ht_search_times.append(ht_search_time)

            # print("{} has {} distinct words".format(filename, ht.size()))
            # print("     (HT) actual count \"the\": {}".format(ht_count))
            # print("     (CMS) estimated count \"the\": {}".format(cms_count))
            actual_counts_sub.append(ht_count)
            estimate_counts_sub.append(cms_count)
            unique_counts_sub.append([ht.size(), ht.size(), 272 * 5])

        iplot.plot(filewordcounts, ht_init_times, 'bo', filewordcounts, ht_init_times, 'b--')
        iplot.plot(filewordcounts, cms_init_times, 'rs', filewordcounts, cms_init_times, 'r--')

        splot.plot(filewordcounts, ht_search_times, 'bo', filewordcounts, ht_search_times, 'b--')
        splot.plot(filewordcounts, cms_search_times, 'rs', filewordcounts, cms_search_times, 'r--')

        actual_counts = actual_counts_sub
        estimate_counts = estimate_counts_sub
        unique_counts = unique_counts_sub

    # Build line graph for time comparisons
    iplot.set_ylabel('Insertion Time (seconds)')
    splot.set_ylabel('Search Time (seconds)')
    splot.set_xlabel('Number of Words Inserted')
    
    # Legend
    red_patch = mpatches.Patch(color='red', label='Count-Min Sketch')
    blue_patch = mpatches.Patch(color='blue', label='Hash Table')
    iplot.legend(handles=[red_patch, blue_patch])
    splot.legend(handles=[red_patch, blue_patch])
    
    fig1.suptitle('CMS vs HashTable Time')
    fig1.savefig('cms_ht_time.png', bbox_inches='tight')


    # Build bar graph for actual vs est comparisons
    x = np.arange(len(filenames))  # the label locations
    width = 0.4  # width of the bars

    fig2, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, actual_counts, width, label='Actual')
    rects2 = ax.bar(x + width/2, estimate_counts, width, label='Estimate')

    ax.set_ylabel('Number of occurrences of \"the\"')
    ax.set_xlabel('Number of total words in input file')
    ax.set_xticks(x)
    ax.set_xticklabels(filewordcounts)
    ax.legend()
    autolabel(rects1)
    autolabel(rects2)
    fig2.tight_layout()
    fig2.suptitle('Actual Count vs Estimated Count')
    fig2.savefig('cms_actual_estimate.png')

    # Build table for space used comparisons
    plt.figure(linewidth=2)
    columns = ('Unique Elements', 'Hash Table', 'CMS')
    rows = ('CSE312', 'Alice in Wonderland', 'Moby Dick', 
               'Count of Monte Cristo', 'War and Peace')
    rcolors = plt.cm.BuPu(np.full(len(rows), 0.1))
    ccolors = plt.cm.BuPu(np.full(len(columns), 0.1))

    table = plt.table(cellText=unique_counts, rowLabels=rows, rowColours=rcolors,
                      rowLoc='right', colColours=ccolors, colLabels=columns, loc='center')
    ax = plt.gca()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.box(on=None)
    plt.suptitle('Space Usage')
    plt.draw()
    fig3 = plt.gcf()
    fig3.tight_layout()
    plt.savefig('space_usage.png', dpi=150)


    