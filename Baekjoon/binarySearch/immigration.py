def solution(n, times):
    answer = int(1e9)
    times.sort()
    s, e = 1 * times[0], n * times[-1]
    while s <= e:
        mid = (s + e) // 2
        counts = []
        for t in times:
            counts.append(mid // t)
        total = sum(counts)
        if total >= n:
            e = mid - 1
            tmp = []
            for i in range(len(times)):
                tmp.append(counts[i] * times[i])
            answer = min(answer, max(tmp))
        else:
            s = mid + 1

    return answer


print(solution(6, [7, 10]))
print(solution(6, [7, 10, 12]))