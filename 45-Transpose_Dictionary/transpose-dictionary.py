# Transpose Dictionary
def solution(scriptByExtension):
    return sorted([[scriptByExtension[x], x] for x in scriptByExtension])
