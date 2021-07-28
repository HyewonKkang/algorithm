S = input()
nums = []
new_str = S[0]
for i in range(1, len(S)):
    if S[i] != S[i-1]:
        nums.append(new_str)
        new_str = S[i]
    else:
        new_str += S[i]
nums.append(new_str)

count_zero = 0
count_one = 0

for n in nums:
    if n[0] == '0':
        count_zero += 1
    else:
        count_one += 1

answer = count_zero if count_zero < count_one else count_one
print(answer)