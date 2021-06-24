def solution(arr):
    def gcd(x, y):
        if y > x:
            min = x
        else:
            min = y
        while (y != 0):
            x, y = y, x % y

        return x
    def lcm(x, y):
        return x * y // gcd(x, y)

    while len(arr) != 1:
        m = arr.pop()
        n = arr.pop()
        arr.append(lcm(m, n))

    return arr[0]

print(solution([2, 6, 8, 14]))
print(solution([1, 2, 3]))