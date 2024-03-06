def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    a, b = 0, 0
    l = len(A)
    while a < l and b < l:
        if A[a] < B[b]:
            answer += 1
            a += 1
            b += 1
        else:
            b += 1
    return answer