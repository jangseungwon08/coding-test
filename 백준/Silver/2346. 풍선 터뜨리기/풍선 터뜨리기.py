import sys
from collections import deque
input = sys.stdin.readline
N = int(input().strip())
paper = list(map(int, input().strip().split()))
dq = deque((i+1, paper[i]) for i in range(N))
ans_list = []
while dq:
    idx , num = dq.popleft()
    ans_list.append(idx)
    # 탈출 조건
    if not dq:
        break
    if num > 0:
        dq.rotate(-(num-1)) #양수일때는 num-1칸 왼쪽으로 회전 (젤 앞 원소가 젤 뒤로 간다)
    else:
        dq.rotate(-num) #음수일때는 -num으로 오른쪽으로 회전
for i in ans_list:
    print(i, end = " ")