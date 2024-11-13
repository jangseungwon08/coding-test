def dfs(v, start):
    visited[v] = 1
    nx_node = arr_list[v][1]

    if nx_node == start:
        return True
    elif visited[nx_node] == 0:
        return dfs(nx_node, start)
    return False

T = int(input())
arr = [0]
for tc in range(1,T+1):
    n = int(input())
    count = 0
    visited = [0] * (n+1)
    arr = list(map(int,input().split()))
    arr_list = [[]for _ in range(n+1)]
    for i in range(1,n+1):
        arr_list[i].append(i)
        arr_list[i].append(arr[i-1])
    for i in range(1,n+1):
        if visited[i] == 0:
            if dfs(i,i):
                count += 1
    print(count)