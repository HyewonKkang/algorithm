S = input()
table = []
for i in range(len(S)):
    for j in range(i+1, len(S)+1):
        table.append(S[i:j])
print(len(set(table)))