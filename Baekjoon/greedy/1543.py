# sol 1
# doc, target = input(), input()
# print(doc.count(target))

# sol 2
doc, target = input(), input()
answer = 0
length = len(target)
idx = 0
for i in range(len(doc)):
    if i < idx:
        continue
    if doc[i:i + length] == target:
        answer += 1
        idx = i + length

print(answer)
