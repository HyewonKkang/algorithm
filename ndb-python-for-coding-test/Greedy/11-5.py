n, m = map(int, input().split())
balls = list(map(int, input().split()))
balls_set = list(set(balls))
res = n * (n - 1) // 2
print(res - len(balls) - len(balls_set))

# n, m = map(int, input().split())
# balls = list(map(int, input().split()))
# res = 0
#
# arr = [0] * (m + 1)
#
# for b in balls:
#     arr[b] += 1
#
# for i in range(1, m + 1):
#     n -= arr[i]
#     res += arr[i] * n
#
# print(res)