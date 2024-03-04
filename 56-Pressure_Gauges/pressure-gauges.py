# Pressure Gauges
def solution(morning, evening):
    return [
        list(map(lambda i: morning[i] if morning[i] < evening[i] else evening[i], range(len(morning)))), 
        list(map(lambda i: morning[i] if morning[i] > evening[i] else evening[i], range(len(morning))))]
