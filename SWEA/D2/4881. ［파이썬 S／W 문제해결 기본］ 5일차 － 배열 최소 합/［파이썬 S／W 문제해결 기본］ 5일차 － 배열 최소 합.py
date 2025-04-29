T = int(input())
for i in range(1,T+1):
    N = int(input())
    N_list = []
    idx_list = []
    col = 0
    num = 0
    minimum = 10000
    for _ in range(N):
        N_list.append(list(map(int,input().split())))
    def backtrack():
        global num, col, minimum
        if len(idx_list) == N:
            minimum = min(minimum, num)
            return 
        for j in range(N):
            if j not in idx_list:
                idx_list.append(j)
                num += N_list[j][col]
                col += 1
                if num < minimum:
                    backtrack()
                idx_list.pop()
                col -= 1
                num -= N_list[j][col]
    backtrack()
    print('#' + str(i), minimum)