def convert_base(N):
    while N >= 1:
        rem = N % 3
        N = N // 3
        if rem == 2:
            rem = -1
            N += 1
        if rem == 0:
            print(0, end=' ')
        else:
            if rem == 1:
                print(1, end=' ')
            else:
                print(-1, end=' ')


N = int(input())
N_base3 = convert_base(N)
