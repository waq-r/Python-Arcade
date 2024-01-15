# Cool Pairs
def solution(a, b):
    uniqueSums = { x+y for y in b for x in a if not (x*y) % (x+y) }
    return len(uniqueSums)
