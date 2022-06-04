def solution(rows, columns, queries):
    answer = []
    table = []
    for i in range(rows):
        tmp = []
        for j in range(columns):
            tmp.append(i * columns + j + 1)
        table.append(tmp)

    for q in queries:
        x_s, y_s, x_e, y_e = q[0] - 1, q[1] - 1, q[2] - 1, q[3] - 1
        tmp = []
        for i in range(y_s, y_e):
            tmp.append(table[x_s][i])
        for i in range(x_s, x_e):
            tmp.append(table[i][y_e])
        for i in range(y_e, y_s, -1):
            tmp.append(table[x_e][i])
        for i in range(x_e, x_s, -1):
            tmp.append(table[i][y_s])

        idx = 0
        for i in range(y_s, y_e):
            table[x_s][i + 1] = tmp[idx]
            idx += 1
        for i in range(x_s, x_e):
            table[i + 1][y_e] = tmp[idx]
            idx += 1
        for i in range(y_e, y_s, -1):
            table[x_e][i - 1] = tmp[idx]
            idx += 1
        for i in range(x_e, x_s, -1):
            table[i - 1][y_s] = tmp[idx]
            idx += 1
        answer.append(min(tmp))

    return answer


print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
print(solution(100, 97, [[1,1,100,97]]))