def solution(wallpaper):
    files_x, files_y = [], []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                files_x.append(j)
                files_y.append(i)
    return [min(files_y), min(files_x), max(files_y) + 1, max(files_x) + 1]
