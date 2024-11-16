for tc in range(1,11):
    N = int(input())
    N_list = []
    count = 0
    for _ in range(8):
        N_list.append(input())
    #가로
    for i in range(8):
        for j in range(9-N):
            s = N_list[i][j:N+j]
            reverse_s = s[::-1]
            if s == reverse_s:
                count += 1
    #세로
    for i in range(8):
        for j in range(9-N):
            s = ''.join(N_list[k][i] for k in range(j, j+N))
            reverse_s = s[::-1]
            if s == reverse_s:
                count += 1
    print('#'+str(tc), count)