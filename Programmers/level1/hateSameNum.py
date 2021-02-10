def solution(arr):
    stack = []
    for i in arr:
        if len(stack) == 0:
            stack.append(i)
        if stack[-1] != i:
            stack.append(i)

    return stack

print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))