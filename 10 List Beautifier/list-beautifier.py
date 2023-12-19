# List Beautifier
def solution(a):
    res = a[:]
    while res and res[0] != res[-1]:
        c, *res, c = res
    return res
