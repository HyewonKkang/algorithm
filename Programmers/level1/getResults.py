# Apr 21, 2022
# def solution(id_list, report, k):
#     answer = []
#     reports = {}
#     counts = {}
#     for id in id_list:
#         reports[id] = []
#         counts[id] = 0
#     for content in report:
#         a, b = content.split()
#         if b not in reports[a]:
#             reports[a].append(b)
#             counts[b] += 1
#
#     for id in id_list:
#         cnt = 0
#         for user in reports[id]:
#             if counts[user] >= k:
#                 cnt += 1
#         answer.append(cnt)
#     return answer

def solution(id_list, report, k):
    answer = [0 for _ in id_list]
    counts = {user: 0 for user in id_list} # 신고된 횟수
    dic = {user: [] for user in id_list} # 유저:신고한 사람 dict
    for r in set(report):
        user, reported = r.split()
        counts[reported] += 1
        dic[user].append(reported)

    for user, reported in dic.items():
        for rId in reported:
            if counts[rId] >= k:
                answer[id_list.index(user)] += 1
    return answer
