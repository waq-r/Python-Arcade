# Cracking Password
from itertools import product

def solution(digits, k, d):
    def createNumber(digs):
        return "".join(map(str, digs))

    return [createNumber(x) for x in filter(lambda e: int(createNumber(e)) % d == 0 , list(sorted(product(digits, repeat=k))))]
