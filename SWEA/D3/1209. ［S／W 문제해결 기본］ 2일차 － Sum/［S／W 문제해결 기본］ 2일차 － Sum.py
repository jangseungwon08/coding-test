for tc in range(1,11):
    n = int(input())
    n_list = []
    sum_di1, sum_di2 = 0, 0,
    row_list, col_list = [], []
    ans_list = []
    for _ in range(100):
        n_list.append(list(map(int, input().split())))
    t_n_list = list(zip(*n_list))
    #행 값
    for i in range(100):
        row_list.append(sum(n_list[i]))
    #열 값
    for i in range(100):
        col_list.append(sum(t_n_list[i]))
    #왼쪽 대각선 아래, 오른쪽 대각선 아래
    for i in range(100):
        j = 99
        sum_di1 += n_list[i][i]
        sum_di2 += n_list[i][j-i]
    ans_list.append(max(row_list))
    ans_list.append(max(col_list))
    ans_list.append(sum_di1)
    ans_list.append(sum_di2)
    print('#'+str(tc), max(ans_list))