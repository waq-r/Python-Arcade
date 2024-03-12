# Check Participants
def solution(participants):
    return [x for x  in range(len(participants)) if participants[x] < x ]
