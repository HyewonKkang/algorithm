num1_s = input()
num2_s = input()
length = max(len(num1_s), len(num2_s))
num1 = int(num1_s, 2)
num2 = int(num2_s, 2)
print(format((num1 & num2), 'b').zfill(length))# 0000001000
print(format((num1 | num2), 'b').zfill(length)) # 0001111111
print(bin(num1 ^ num2)[2:].zfill(length)) # 0001110111

def not_operator(n):
    n= str(n)
    value = ''
    for w in n:
        if w == '0':
            value += '1'
        else:
            value += '0'
    return value

print(not_operator(num1_s)) # 1110100111
print(not_operator(num2_s)) # 1111010000