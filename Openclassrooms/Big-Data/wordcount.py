#! /usr/bin/env python

from pyspark import SparkContext

sc = SparkContext()

lines = sc.textFile("/Users/marcpartensky/Programs/Python/Machine-Learning/Openclassrooms/Big-Data/text.txt")

word_counts = lines.flatMap(lambda line: line.split(' ')) \
        .map(lambda word: (word, 1)) \
        .reduceByKey(lambda count1, count2: count1+count2) \
        .collect()

for (word, count) in word_counts:
    print(word.encode("utf8"), count)
