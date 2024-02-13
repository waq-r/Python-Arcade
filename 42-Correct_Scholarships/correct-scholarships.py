# Correct Scholarships
def solution(bestStudents, scholarships, allStudents):
    return scholarships is not None and set(bestStudents) <= set(scholarships) < set(allStudents) 
