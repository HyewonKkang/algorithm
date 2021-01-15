N, S = map(int, input().split())
nums = list(map(int, input().split()))
def powerset(N, S, nums):
    if S == 0:
        answer = -1
    else:
        answer = 0
    for i in range(1 << N):
        subset = []
        for j in range(N):
            if i & (1 << j):
                subset.append(nums[j])
        if sum(subset) == S:
            answer += 1
    return answer

print(powerset(N, S, nums))