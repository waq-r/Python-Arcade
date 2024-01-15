# Word Power
def solution(word):
    num = {v:k for k,v in enumerate([c for c in 'abcdefghijklmnopqrstuvwxyz'], start=1)}
    return sum([num[ch] for ch in word])
