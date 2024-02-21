# Frequency Analysis
from collections import Counter

def solution(encryptedText):
    return max(Counter(encryptedText), key = lambda k: Counter(encryptedText)[k])
