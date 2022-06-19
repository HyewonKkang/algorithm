def solution(cards):
    scores = []
    length = len(cards)
    trade = [False] * length

    for card_set in cards:
        value = min(card_set)
        scores.append([card_set.index(value), value])

    for i in range(length):
        if trade[i]: continue
        for j in range(i + 1, length):
            if trade[i]:
                continue
            if cards[i][scores[j][0]] - 1 > scores[i][1] and cards[j][scores[i][0]] + 1 > scores[j][1]:
                trade[i] = True
                trade[j] = True
                cards[i][scores[j][0]] -= 1
                cards[j][scores[i][0]] -= 1
                scores[i][1] += 1
                scores[j][1] += 1
    answer = 0
    for score in scores:
        answer += score[1]
    return answer

