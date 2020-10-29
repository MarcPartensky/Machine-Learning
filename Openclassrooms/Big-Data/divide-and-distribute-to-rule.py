#!/usr/bin/env python

from collections import defaultdict


text = "pour rendre le fonctionnement de mapreduce plus concret, nous allons \
l'illustrer avec word count l'exemple typique de mapreduce, si typique qu'il en \
est devenu le hello world de mapreduce et du calcul distribué"

def word_count(text):
    counts = defaultdict(int)
    for word in text.split():
        counts[word.lower()] += 1
    return counts

print(word_count(text))


def map(key, value):
    intermediate = []
    for i in value:
        intermediate.append(i[1], (i[0], i[1:])))
    return intermediate
