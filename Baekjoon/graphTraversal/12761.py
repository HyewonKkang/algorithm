import sys
from collections import deque

input = sys.stdin.readline
a, b, n, m = map(int, input().split())
cnt = [0] * 100001

def bfs():
    q = deque([n])
    while q:
        now = q.popleft()
        if now == m:
            print(cnt[now])
            break
        for i in (now+1, now-1, now+a, now+b, now-a, now-b, now*a, now*b):
            if 0 <= i <= 100000 and cnt[i] == 0:
                cnt[i] = cnt[now] + 1
                q.append(i)


bfs()