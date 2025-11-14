def solution(wallpaper):
    answer = [0,0,0,0]
    # 행 중에 젤 작은 값 + 열 중에 젤 작은 값
    # 행 중에 젤 큰 값 + 열 중에 젤 큰 값
    min_row, min_col, max_row, max_col = len(wallpaper), len(wallpaper[0]), 0, 0
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                min_row = min(min_row, i)
                min_col = min(min_col, j)
                max_row = max(max_row, i)
                max_col = max(max_col, j)
    answer[0], answer[1], answer[2], answer[3] = min_row, min_col, max_row+1, max_col+1
    return answer