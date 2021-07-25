N = int(input())
answer = 0
distance = list(map(int, input().split()))
prices = list(map(int, input().split()))

min_price = prices[0]
answer += distance[0] * prices[0]

i = 1
while i != N-1:
    if prices[i] > min_price:
        answer += distance[i] * min_price
    else:
        min_price = prices[i]
        answer += distance[i] * min_price
    i += 1
print(answer)