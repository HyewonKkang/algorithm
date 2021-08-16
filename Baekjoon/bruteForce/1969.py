N, M = map(int, input().split())
answer = ''
hd = 0
dna = [input() for i in range(N)]

for i in range(M):
    counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for j in range(N):
        counts[dna[j][i]] += 1
    tmp = []
    largest = 'A'
    for key in counts:
        if counts[largest] < counts[key]:
            largest = key
    answer += largest
    hd += N - counts[largest]


print(answer)
print(hd)