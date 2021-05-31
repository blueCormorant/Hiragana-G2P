#!/usr/bin/env python
from Levenshtein import distance as lev


def pairwise(iterable):
    a = iter(iterable)
    return zip(a, a)


with open("out.txt", "r") as _file:
    errors = []
    for line in _file:
        if not line[:2] == "--":
            errors.append(line[2:].strip())

_sum = 0
for transcribed, gold in pairwise(errors):
    _sum = _sum + lev(transcribed, gold)

msg = f"""Out of {round(len(errors)/2)} errors, the average edit distance was {_sum/(len(errors)/2)}"""
print(msg)
