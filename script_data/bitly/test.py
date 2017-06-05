#!/usr/bin/env python

fn = 'bitly.tsv'
numset = set()
count = 0
for line in open(fn):
    count += 1
    numset.add(len(line.split('\t')))

print numset
print count
