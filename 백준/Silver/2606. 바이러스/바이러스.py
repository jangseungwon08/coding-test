N = int(input())
M = int(input())
N_list = [[] for i in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
    a, b = map(int,input().split())
#방향성이 없으므로 양쪽 연결
    N_list[a].append(b)
    N_list[b].append(a)
#방문할 컴퓨터 번호 v
def dfs(v):
    visited[v] = 1
    #N_list[v]는 v번 컴퓨터에 연결된 리스트
    #N_lsit[v]의 원소값에 i가 0이면 dfs(i)를 재귀호출
    #ex) i = 2이면 visited[2] == 0이면 dfs(2)를 실행하여 N_list[2]의 원소에 접근하여 다시 순회
    for i in N_list[v]:
        if visited[i] == 0:
            dfs(i)
dfs(1)
print(sum(visited)-1)