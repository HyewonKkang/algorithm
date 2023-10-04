from collections import Counter


def solution(weights):
    answer = 0
    counts = Counter(weights)
    for w in counts:
        if w * 2/3 in weights:
            answer += counts[w * 2/3] * counts[w]
        if w * 3/4 in weights:
            answer += counts[w * 3/4] * counts[w]
        if w * 2/4 in weights:
            answer += counts[w * 2/4] * counts[w]

    for k, v in counts.items():
        if v > 1:
            answer += v * (v-1) / 2
    return int(answer)
