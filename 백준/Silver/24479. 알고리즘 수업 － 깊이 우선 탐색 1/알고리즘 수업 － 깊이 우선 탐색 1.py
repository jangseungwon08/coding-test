import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline
N ,M, R = map(int,input().split())
node = [[] for _ in range(N+1)]
result = [0] * (N+1)
visited = [0] *(N+1)
for _ in range(M):
    u,v = map(int,input().split())
    #무방향 그래프이기때문에 연결된 노드들은 해당 노드번호에 
    #바꿔서 넣어준다
    node[u].append(v)
    node[v].append(u)
#인접정점은 오름차순으로 방문한다고 했으니 오름차순 정렬해준다.
for i in range(N+1):
    node[i].sort()
def dfs(r):
    global count
    visited[r] = count
    result[r] = count
    count += 1
    for j in node[r]:
        #방문하지 않은 노드가 있으면 재귀호출로 다음 노드로 
        if visited[j] == 0:
            dfs(j)
count = 1
dfs(R)
for i in range(1,len(result)):
    print(result[i])