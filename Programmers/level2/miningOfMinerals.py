def solution(picks, minerals):
    answer = [int(1e9)]
    counts = picks[:]

    def lossHp(tool, mineral):
        if tool == 0:
            return 1
        elif tool == 1:
            if mineral == "diamond":
                return 5
            else:
                return 1
        elif tool == 2:
            if mineral == "diamond":
                return 25
            elif mineral == "iron":
                return 5
            else:
                return 1

    def dfs(counts, hp, m):
        if not any(counts) or m == len(minerals):
            answer[0] = min(answer[0], hp)
            return

        for i in range(3):
            if counts[i] > 0:
                counts[i] -= 1
                tmp = 0
                m_ = m
                for j in range(m, m + 5):
                    if j >= len(minerals): break
                    m = j
                    tmp += lossHp(i, minerals[j])
                dfs(counts, hp + tmp, m + 1)
                counts[i] += 1
                m = m_


    dfs(counts, 0, 0)

    return answer[0]
