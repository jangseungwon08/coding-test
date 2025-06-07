from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
M = int(input())
C = list(map(int,input().split()))
q = deque([])

for i in range(N):
    # 큐인 자료구조만 모아주기기
    if A[i] == 0:
        q.append(B[i])

#오른쪽으로 갈 수록 나중에 들어온 값으로 처리했다.
# ex) deque([1,4])
#  --> deque([2,1,4]) -> deque([2,1]) 
# why? -> stack은 append pop하면 stack의 특성상 LIFO이기때문에 자기자신을 
# 넣고 빼기 때문에 stack은 상관이 없다
for i in range(M):
    q.appendleft(C[i])
    print(q.pop(), end = ' ')