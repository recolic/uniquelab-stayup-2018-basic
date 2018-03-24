#!/usr/bin/env python3
from functools import reduce

with open('/dev/fd/0', 'r') as fd:
    cont = fd.read()

res = []
for line in cont.split('\n'):
    if line == '':
        continue
    ar = line.split('/')
    solu, ans = float(ar[0]), float(ar[1])
    if solu <= 0 or ans <= 0:
        continue
    res.append(solu/ans)

print("Predict res: AVG", reduce(lambda x, y: x+y, res) / len(res), 
        "MAX", reduce(lambda x, y: max(x, y), res), 
        "MIN", reduce(lambda x, y: min(x, y), res) )

