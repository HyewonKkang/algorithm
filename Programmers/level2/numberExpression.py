def solution(n):
    answer = 0
    sum = 0
    for i in range(1, n): # 덧셈의 시작
        sum = 0
        for j in range(i+1, n+1):
            sum += j
            if sum > n:
                break
            elif sum == n:
                answer += 1
                break

    return answer

print(solution(15))