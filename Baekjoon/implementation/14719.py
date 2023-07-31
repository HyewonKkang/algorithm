h, w = map(int, input().split())
heights = list(map(int, input().split()))
total = 0

for i in range(1, w - 1):
    left = max(heights[:i])
    right = max(heights[i + 1:])
    h_ = min(left, right)
    if h_ > heights[i]:
        total += h_ - heights[i]
print(total)