n = int(input())
nums = []

def backtracking(num):
    last = num[-1]
    nums.append(int(num))
    for i in range(int(last)):
        backtracking(num + str(i))

for i in range(0, 10):
    backtracking(str(i))

nums.sort()
print(nums[n - 1] if n - 1 < len(nums) else -1)
