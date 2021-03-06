x, y, w, h = map(int, input().split())

result = min(min(w-x, x), min(h-y, y))
print(result)