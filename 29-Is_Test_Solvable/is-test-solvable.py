# Is Test Solvable
def solution(ids, k):
    digitSum = lambda n: 0 if n == 0 else (n % 10) + digitSum(int(n / 10))

    sm = 0
    for questionId in ids:
        sm += digitSum(questionId)
    return sm % k == 0
