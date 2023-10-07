def getDiffCount(a, b):
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1
    return cnt


def isAvailable(cur, next):
    if getDiffCount(cur, next) == 1: return True
    return False


def solution(begin, target, words):
    answer = [int(1e9)]

    if target not in words:
        return 0

    def backtracking(cur, count, visited):
        if cur == target:
            answer[0] = min(answer[0], count)
            return
        for w in words:
            if w != cur and w not in visited and isAvailable(cur, w) :
                visited.append(w)
                backtracking(w, count + 1, visited)
                visited.remove(w)

    backtracking(begin, 0, [])

    return answer[0] if answer[0] != int(1e9) else 0
