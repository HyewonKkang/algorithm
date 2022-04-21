def solution(id_list, report, k):
    answer = []
    reports = {}
    counts = {}
    for id in id_list:
        reports[id] = []
        counts[id] = 0
    for content in report:
        a, b = content.split()
        if b not in reports[a]:
            reports[a].append(b)
            counts[b] += 1

    for id in id_list:
        cnt = 0
        for user in reports[id]:
            if counts[user] >= k:
                cnt += 1
        answer.append(cnt)
    return answer


print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))