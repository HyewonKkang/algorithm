from collections import deque

def solution(coin, cards):
    answer = 1
    n = len(cards)
    owned = cards[:n // 3]
    left = deque(cards[n // 3:])
    possible = []

    def canProgress(src, dst):
        for x in src:
            if n + 1 - x in dst:
                src.remove(x)
                dst.remove(n + 1 - x)
                return True
        return False

    while left:
        possible.append(left.popleft())
        possible.append(left.popleft())

        if canProgress(owned, owned):
            answer += 1
        elif canProgress(owned, possible) and coin >= 1:
            answer += 1
            coin -= 1
        elif canProgress(possible, possible) and coin >= 2:
            answer += 1
            coin -= 2
        else:
            break

    return answer


print(solution(4, [3, 6, 7, 2, 1, 10, 5, 9, 8, 12, 11, 4]))
print(solution(3, [1, 2, 3, 4, 5, 8, 6, 7, 9, 10, 11, 12]))
print(solution(2, [5, 8, 1, 2, 9, 4, 12, 11, 3, 10, 6, 7]))
print(solution(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]))