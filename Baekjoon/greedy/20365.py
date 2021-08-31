N = int(input())
colors = input()
answer = 1
current = colors[0]
i = 0
nums = {'B':0, 'R':0}
while i != len(colors):
    if colors[i] != current:
        nums[current] += 1
        current = colors[i]
    i += 1
nums[current] += 1
print(min(nums['B'], nums['R']) + 1)