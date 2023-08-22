def solution(targets):
    answer = 0
    targets.sort()
    overlapped = targets[0]
    for t in targets[1:]:
        if overlapped[1] > t[0]:
            overlapped = [max(overlapped[0], t[0]), min(overlapped[1], t[1])]
        else:
            overlapped = t
            answer += 1
    return answer + 1
