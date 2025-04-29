T = int(input())
for i in range(1,T+1):
    V, E = map(int, input().split())
    # 인접행렬로 그래프 초기화
    graph = [[0] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        sn, en = map(int, input().split())
        graph[sn][en] = 1
    S, G = map(int,input().split())

    def dfs(s, e):
        stack = [s]
        visit = [False] * (V+1)

        while stack:
            now = stack.pop()
            if not visit[now]:
                visit[now] = True
                for next in range(1, V+1):
                    if graph[now][next] and not visit[next]:
                        stack.append(next)

        return 1 if visit[e] else 0
    print('#'+str(i),dfs(S,G))
