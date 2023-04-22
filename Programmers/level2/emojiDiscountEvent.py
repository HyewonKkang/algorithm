from itertools import product


def getPercentage(rate):
    return 1 - rate / 100


def solution(users, emoticons):
    answer = []
    discounts = [10, 20, 30, 40]
    for perm in list(product(discounts, repeat=len(emoticons))):
        rates = list(perm)
        prices = [int(round(getPercentage(rates[i]) * emoticons[i], 0)) for i in range(len(emoticons))]
        plus, earned = 0, 0

        for percent, criteria in users:
            purchased = 0
            for i in range(len(emoticons)):
                if percent <= rates[i]:
                    purchased += prices[i]
            if purchased >= criteria:
                plus += 1
            else:
                earned += purchased

        answer.append([plus, earned])

    return max(answer, key=lambda x: (x[0], x[1]))
