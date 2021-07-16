def solution(s):
    answer = []
    s = s[2:-2]
    tuples = []

    for tmp in s.split('},{'):
        tuples.append(tmp.split(','))

    tuples.sort(key=len)
    d = {}
    for num in tuples[-1]:
        d[num] = 1

    for nums in tuples[0:-1]:
        for n in nums:
            d[n] += 1

    new_d = sorted(d.items(), key=lambda x:x[1], reverse=True) # 딕셔너리 내림차순 정렬
    for (key, value) in new_d:
        answer.append(int(key))
    return answer
