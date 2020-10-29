#! /usr/bin/env python

import sys
from pyspark import SparkContext

sc = SparkContext()

lines = sc.textFile(sys.argv[1])
words = lines.flatMap(lambda line: line.split(' '))
words_with_1 = words.map(lambda word: (word, 1))
word_counts = words_with_1.reduceByKey(
    lambda count1, count2: count1 + count2
)

result = word_counts.collect()

for word, count in result:
    print(word.encode('utf8'), count)
