a, b, c, d, e, f = map(int, input().split())

x = (b * f - c * e) // (b * d - a * e)
y = (a * f - c * d) // (a * e - b * d)

print(x, y)

# a, b, c, d, e, f = map(int, input().split())
# left = b * d - e * a
# right = c * d - f * a
#
# if left == 0:
#     y = -1 * left // right
# else:
#     y = right // left
#
# left = a * e - d * b
# right = c * e - f * b
# if left == 0:
#     x = -1 * right // left
# else:
#     x = right // left
#
# print(x, y)
#
