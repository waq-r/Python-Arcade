# Least Common Denominator
from math import gcd

def solution(denominators):
    return functools.reduce(lambda a,v: int(a * v / gcd(a,v)) , denominators)
