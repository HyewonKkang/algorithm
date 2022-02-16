N = int(input())
components = list(map(int, input().split()))
M = int(input())
request = list(map(int, input().split()))
components.sort()

def binary_search(target, start, end):
    if start > end:
        return False
    mid = (start + end) // 2
    if target == components[mid]:
        return True
    elif components[mid] > target:
        return binary_search(target, start, mid - 1)
    else:
        return binary_search(target, mid + 1, end)

for i in range(M):
    if binary_search(request[i], 0, N - 1):
        print('yes', end = ' ')
    else:
        print('no', end = ' ')