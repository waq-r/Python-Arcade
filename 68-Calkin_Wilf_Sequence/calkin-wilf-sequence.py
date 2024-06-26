# Calkin Wilf Sequence
def solution(number):
    def fractions():
        a = 1
        b = 1
        while True:
            yield [a, b]
            a, b = b, 2 * (a - a % b) + b - a

    gen = fractions()
    res = 0
    while next(gen) != number:
        res += 1
    return res
