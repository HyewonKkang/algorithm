def solution(n):
    answer = []
    input = list(str(n))
    for _ in range(len(input)):
        answer.append(int(input.pop()))
    return answer