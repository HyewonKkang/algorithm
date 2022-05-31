def solution(number, k):
    stack = [number[0]]
    for n in number[1:]:
        while stack and stack[-1] < n and k > 0:
            k -= 1
            stack.pop()
        stack.append(n)

    return ''.join(stack[:len(stack) - k])
