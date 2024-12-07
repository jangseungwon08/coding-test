from collections import deque
n = int(input())
n_list = deque()
for i in range(1,n+1):
    n_list.append(i)
while len(n_list) != 1:
    n_list.popleft()
    top = n_list.popleft()
    n_list.append(top)
n_list = list(n_list)
ans = n_list[0]
print(ans)