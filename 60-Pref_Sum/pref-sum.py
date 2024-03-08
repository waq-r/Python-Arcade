# Pref Sum
def solution(a):
    return functools.reduce(lambda x,y:x+[sum(x[-1:]+[y])],a,[])
