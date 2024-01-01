# Get Commit
def solution(commit):
    return re.sub(r"^[0\?\+\!]{0,}", '', commit)
