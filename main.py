#!/usr/bin/env python3

from collections import defaultdict
import itertools

DICTIONARIES = [
    '/usr/share/dict/american-english',
    '/usr/share/dict/british-english'
]

X = set()
d = defaultdict(list)

for lw in DICTIONARIES:
    with open(lw) as f:
        X = X.union(map(lambda x: x.strip().lower(), f.readlines()))

for word in X:
    d[len(word)].append(word)

for x, y, z in list(filter(lambda x: sum(x) == 8, itertools.permutations(range(1, 7), 3))):
    for fw in d[x]:
        for sw in d[y]:
            for tw in d[z]:
                print(" ".join([fw, sw, tw]))
