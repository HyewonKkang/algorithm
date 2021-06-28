import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while True:
        if len(scoville) <= 1 and scoville[0] < K:
            answer = -1
            break
        if scoville[0] >= K:
            break
        else:
            num = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
            heapq.heappush(scoville, num)
            answer += 1

    return answer
