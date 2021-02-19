def solution(arr):
    answer = []
    if len(arr) == 1:
        return [-1]
    delNum = min(arr)
    for i in arr:
        if i != delNum:
            answer.append(i)
    return answer