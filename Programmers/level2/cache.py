from collections import deque
def solution(cacheSize, cities):
    answer = 0
    city = []
    cache = deque()
    for place in cities:
        city.append(place.lower())
    for place in city:
        if place not in cache:
            answer += 5
            if cacheSize != 0:
                if len(cache) < cacheSize:
                    cache.append(place)
                else:
                    cache.popleft()
                    cache.append(place)
        else:
            answer += 1
            del cache[cache.index(place)]
            cache.append(place)

    return answer