import itertools
def solution(citations):
    answer = 0
    citations.sort(reverse=True)

    for h in range(len(citations), -1, -1):
        cnt = 0
        for num in citations:
            if num >= h:
                cnt += 1
        if cnt >= h:
            answer = h
            break


    return answer