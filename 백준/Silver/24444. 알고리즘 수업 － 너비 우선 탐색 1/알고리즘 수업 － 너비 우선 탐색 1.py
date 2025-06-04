from collections import deque
import sys
input = sys.stdin.readline
N, M , R = map(int, input().split())
node = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
    u, v = map(int, input().split())
    node[u].append(v)
    node[v].append(u)

for i in range(N+1):
    node[i].sort()

q = deque()
q.append(R)
visited[R] = 1
count =2
while q:
    line = q.popleft()
    for i in node[line]:
        if not visited[i]:
            visited[i] = count
            count += 1
            q.append(i)
for i in range(1,N+1):
    print(visited[i])