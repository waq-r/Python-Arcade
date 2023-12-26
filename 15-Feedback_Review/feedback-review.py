# Feedback Review
import textwrap

def solution(feedback, size):
    return filter(None, textwrap.fill(feedback, size).split("\n"))
