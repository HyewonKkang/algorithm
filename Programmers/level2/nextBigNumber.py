def solution(n):
    answer = 0
    binary = str(bin(n))
    num = binary.count('1')
    tmp = 0
    startNum = n + 1
    while(True):
        binary2 = str(bin(startNum))
        num2 = binary2.count('1')
        if(num == num2):
            answer = startNum
            break
        startNum += 1
    return answer

print(solution(78))
print(solution(15))