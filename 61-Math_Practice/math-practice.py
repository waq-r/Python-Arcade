# Math Practice
def solution(numbers):
    return functools.reduce(lambda a, v: (a + v[1] if v[0] % 2 else a * v[1])   , enumerate(numbers), 1 )
