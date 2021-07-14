def ranking(num):
    if num < 2:
        return 6
    return 7 - num

def solution(lottos, win_nums):
    answer = [0, 0]

    for num1 in lottos:
        for num2 in win_nums:
            if num1 == 0:
                answer[0] += 1
                break
            if num1 == num2:
                answer[0] += 1
                answer[1] += 1
                break

    answer[0] = ranking(answer[0])
    answer[1] = ranking(answer[1])

    return answer