# Words Recognition
def solution(word1, word2):
    def getIdentifier(w1, w2):
        return ''.join(sorted([x for x in set(w1) - set(w2)]))

    return [getIdentifier(word1, word2), getIdentifier(word2, word1)]
