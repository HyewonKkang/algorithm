import heapq
def solution(operations):
    q = []
    for op in operations:
        if op.startswith('I'):
            tmp = op.split()
            heapq.heappush(q, int(tmp[1]))
        elif op.startswith('D'):
            tmp = op.split()
            if tmp[1].startswith('-'):
                if q:
                    heapq.heappop(q)
            else:
                if q:
                    tmp = []
                    for i in q:
                        heapq.heappush(tmp, -i)
                    heapq.heappop(tmp)
                    q = []
                    for i in tmp:
                        heapq.heappush(q, -i)
        print(q)
    if not q: return [0, 0]
    else:
        return [max(q), min(q)]
