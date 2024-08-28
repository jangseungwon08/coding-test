def solution(arr):
    answer = []
    temp_col = len(arr[0])
    temp_row = len(arr)
    if temp_col < temp_row:
        for i in arr:
            answer.append(i+[0]*(temp_row-temp_col))
        return answer
    elif temp_col > temp_row:
        for _ in range(temp_col-temp_row):
            arr.append([0]*temp_col)
        return arr
    else:
        return arr