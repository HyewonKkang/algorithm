def solution(line):
    answer = []
    keyboards = [['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
                 ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P']]
    left, right = (1, 0), (1, 9)

    for l in line:
        pos = (0,0)
        for i in range(2):
            for j in range(10):
                if l == keyboards[i][j]:
                    pos = (i, j)
        left_distance = abs(pos[0] - left[0]) + abs(pos[1] - left[1])
        right_distance = abs(pos[0] - right[0]) + abs(pos[1] - right[1])
        if left_distance - right_distance != 0:
            if left_distance > right_distance: answer.append(1)
            else: answer.append(0)
        else:
            left_hor_distance =  abs(pos[1] - left[1])
            right_hor_distance =  abs(pos[1] - right[1])
            if left_hor_distance - right_hor_distance != 0:
                if left_hor_distance > right_hor_distance:
                    answer.append(1)
                else:
                    answer.append(0)
            else:
                if pos[1] <= 4:
                    answer.append(0)
                else:
                    answer.append(1)
        if answer[-1] == 0:
            left = (pos[0], pos[1])
        else:
            right = (pos[0], pos[1])

    return answer


print(solution("Q4OYPI"))
print(solution("RYI76"))
print(solution("64E2"))