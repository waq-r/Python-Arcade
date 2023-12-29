# Competitive Eating
def solution(t, width, precision):
    return ('%.*f' % (precision, t)).center(width)
