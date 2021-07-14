def putZero(num):
    if len(num) == 1:
        return '0' + num
    return num

h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))

t1 = h1 * 60 * 60 + m1 * 60 + s1
t2 = h2 * 60 * 60 + m2 * 60 + s2

t = t2 - t1
hours = t // 60 // 60
minutes = t // 60
seconds = t % 60

answer = putZero(hours) + ':' + putZero(minutes) + ':' + putZero(seconds)
