import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
dq = deque([])
for _ in range(N):
    put = input().strip()
    if len(put) > 2:
        if put[0] == '1':
            dq.appendleft(int(put[2:]))
        elif put[0] == '2':
            dq.append(int(put[2:]))
    else:
        if put == '3':
            if dq:
                print(dq.popleft())
            else:
                print(-1)
        elif put == '4':
            if dq:
                print(dq.pop())
            else:
                print(-1)
        elif put == '5':
            print(len(dq))
        elif put == '6':
            if dq:
                print(0)
            else:
                print(1)
        elif put == '7':
            if dq:
                print(dq[0])
            else:
                print(-1)
        elif put == '8':
            if dq:
                print(dq[-1])
            else:
                print(-1)