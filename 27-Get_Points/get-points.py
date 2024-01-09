# Get Points
def solution(answers, p):
    questionPoints = lambda i,a: i+1 if a else -p

    res = 0
    for i, ans in enumerate(answers):
        res += questionPoints(i, ans)
    return res
