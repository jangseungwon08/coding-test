T= int(input())
for tc in range(1,T+1):
    n, l = map(int,input().split())
    n_list = []
    ans_list = []
    max_taste = 0
    def dfs(i, taste, kcal):
        global max_taste
        if kcal > l:
            return
        if taste > max_taste:
            max_taste = taste
        if i == n:
            return
        dfs(i + 1, taste + n_list[i][0], kcal + n_list[i][1])
        dfs(i+1, taste, kcal)
    for _ in range(n):
        n_list.append(list(map(int,input().split())))
    dfs(0,0,0)
    print('#'+str(tc),max_taste)