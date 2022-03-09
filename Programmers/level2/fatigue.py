from itertools import permutations
def solution(k, dungeons):
    max = 0
    val = k
    for lists in permutations(dungeons, len(dungeons)):
        tmp = 0
        k = val
        for i in range(len(list(lists))):
            if k >= lists[i][0]:
                k -= lists[i][1]
                tmp += 1
        if max <= tmp:
            max = tmp
    return max

print(solution(80, [[80,20],[50,40],[30,10]]))