# Multiplication Table
def solution(n):
    return [[y*x for y in range(1,n+1)] for x in range(1, n+1)]
