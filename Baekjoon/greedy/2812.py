n, k = map(int, input().split())
numbers = input()
stack = [numbers[0]]

for num in numbers[1:]:
    while stack and stack[-1] < num and k:
        k -= 1
        stack.pop()
    stack.append(num)

print(''.join(stack[:len(stack) - k]))