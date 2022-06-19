from itertools import combinations

def solution(prices, d, k):
    answer = 0
    prices.sort()
    length = len(prices)

    if prices[-1] - prices[0] <= d:
        answer = sum(prices) // len(prices)
    elif prices[-2] - prices[1] <= d:
        answer = sum(prices[1:length - 1]) // (len(prices) - 2)
    else:
        flag = 0
        tmp_avg = prices[-1]
        for comb in list(combinations(prices, k)):
            if max(comb) - min(comb) <= d:
                tmp_avg = min(tmp_avg, sum(comb) // len(comb))
                flag = 1
        if flag == 0:
            if length % 2:
                answer = prices[length // 2]
            else:
                answer = prices[length // 2 - 1]
    return answer