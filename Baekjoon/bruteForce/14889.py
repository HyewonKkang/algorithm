from itertools import combinations

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
answer = int(1e9)
members = [i for i in range(n)]

for teamA in list(combinations(members, n // 2)):
    teamAScore = 0
    for i in range(len(teamA)):
        for j in range(len(teamA)):
            if i != j:
                teamAScore += s[teamA[i]][teamA[j]]
    teamB = [i for i in members if i not in teamA]
    teamBScore = 0
    for i in range(len(teamB)):
        for j in range(len(teamB)):
            if i != j:
                teamBScore += s[teamB[i]][teamB[j]]
    answer = min(answer, abs(teamAScore - teamBScore))
print(answer)