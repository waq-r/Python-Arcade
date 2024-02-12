# Unique Characters
def solution(document):
    return sorted(list(dict.fromkeys([x for x in document])))
