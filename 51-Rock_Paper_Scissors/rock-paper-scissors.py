# Rock Paper Scissors
from itertools import permutations

def solution(players):
    return sorted(set([x for x in permutations(players, 2)]))
