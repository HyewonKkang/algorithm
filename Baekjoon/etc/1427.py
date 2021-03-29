nums = input()
arr = []
for i in nums:
    arr.append(i)
arr.sort(reverse=True)
print(''.join(arr))