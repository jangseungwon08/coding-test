import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().strip().split())
N_list = deque([i for i in range(1,N+1)])
ans_list = []

while N_list:
    for _ in range(K-1):
        # 2번만큼 popleft시켜서 append (FIFO 완벽하게 만족)
        N_list.append(N_list.popleft())
    # 그리고 3번째에 나오는 값을 popleft함수로 ans_list에 append
    ans_list.append(N_list.popleft())
print("<", end = "")
for i in range(N):
    if i == N-1:
        print(ans_list[i], end = ">")
    else:
        print(ans_list[i], end = ", ")