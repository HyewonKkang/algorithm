import sys

string = sys.stdin.readline().rstrip()
lst = list(string)
res = ['' for _ in range(len(lst))]

def findSide(arr, start):
    if not arr:
        return
    min_value = min(arr)
    min_idx = arr.index(min_value)
    res[start + min_idx] = min_value
    print(''.join(res))

    findSide(arr[min_idx + 1:], start + min_idx + 1)
    findSide(arr[:min_idx], start)


findSide(lst, 0)