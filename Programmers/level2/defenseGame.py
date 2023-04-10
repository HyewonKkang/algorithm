import heapq


def solution(n, k, enemy):
    answer = 0
    heap = []

    if k >= len(enemy):
        return len(enemy)

    for i, e in enumerate(enemy):
        heapq.heappush(heap, -e)
        n -= e
        if n < 0:
            if k <= 0: break
            else:
                n -= heapq.heappop(heap)
                k -= 1
        answer += 1

    return answer
