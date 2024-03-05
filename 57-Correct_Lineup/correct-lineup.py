# Correct Lineup
def solution(athletes):
    return functools.reduce(lambda x,y: x+y, [[athletes[i+1], athletes[i]] for i in range(0, len(athletes)+1 //2, 2)])
