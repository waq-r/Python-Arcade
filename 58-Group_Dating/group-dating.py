# Group Dating
def solution(male, female):
    return [[male[x] for x in range(len(male)) if male[x] != female[x]], [female[x] for x in range(len(female)) if male[x] != female[x]]]
