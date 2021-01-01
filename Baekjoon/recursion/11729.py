def move(n, start, to):
    print(start, to)

def hanoi(n, start, to, via):
     # 탈출 조건
    if n == 1:
        move(1, start, to)
        return
    # 원반 n-1개를 보조기둥으로 이동
    hanoi(n-1, start, via, to)
    # 가장 큰 원반을 목적지로 이동
    move(n, start, to)
    # 보조기둥에 있는 원반 n-1개를 목적지로 이동
    hanoi(n-1, via, to, start)

n = int(input())
print(2**n - 1)
hanoi(3, 1, 3, 2)