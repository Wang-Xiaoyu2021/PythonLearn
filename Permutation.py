#!/usr/bin/env python

import itertools

b = []
for i in itertools.permutations('AABB', 4):
    b.append(i)
print(b)
print(list(set(b)))