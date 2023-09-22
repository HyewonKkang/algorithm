def solution(dirs):
    moveByPath = {'U':(0, 1), 'L':(-1, 0), 'R':(1, 0), 'D':(0, -1)}
    visited = []
    x, y = 0, 0
    for d in dirs:
        dx, dy = moveByPath[d]
        nx, ny = x + dx, y + dy
        if nx < -5 or nx > 5 or ny < -5 or ny > 5: continue
        visited.append((x, y, nx, ny))
        visited.append((nx, ny, x, y))
        x, y = nx, ny
    return len(set(visited)) // 2
