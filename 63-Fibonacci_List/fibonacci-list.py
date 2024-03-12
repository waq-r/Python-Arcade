# Fibonacci List
def solution(n):
    return [[0] * x for x in functools.reduce((lambda a, b: a+[a[-1] + a[-2]]), range(2, n), [0,1])]
