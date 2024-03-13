# Primes Sum
def solution(a, b):
    return sum([p for p in range(max(a,2), b+1) if not 0 in [p%x for x in range(2, int(p**0.5)+1 )]])
