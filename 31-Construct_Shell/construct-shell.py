# Construct Shell
def solution(n):
    return [[0]*(min(i, n+n-i)) for i in range(1, n+n)]
