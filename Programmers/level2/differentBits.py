def solution(numbers):
    answer = []
    for n in numbers:
        str_bin = str(bin(n)[2:])
        if str_bin[-1] == '0':
            str_bin = str_bin[:-1] + '1'
        else:
            if '0' in str_bin:
                for i in range(len(str_bin)-1, -1, -1):
                    if str_bin[i] == '0':
                        if str_bin[i+1] == '1':
                            str_bin = str_bin[:i] + '10' + str_bin[i+2:]
                        else:
                            str_bin = str_bin[:i] + '1' + str_bin[i+1:]
                        break
            else:
                str_bin = '10' + str_bin[1:]
        answer.append(int('0b' + str_bin, 2))
    return answer
