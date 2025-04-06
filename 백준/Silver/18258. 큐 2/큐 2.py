import sys
from collections  import deque

input = sys.stdin.readline
N = int(input())
queue = deque([])
for _ in range(N):
    questr = str(input().rstrip())
    if "push" in questr:
        queue.append(questr[5:])
    elif questr == 'pop':
        if queue:
            num = queue.popleft()
            print(num)
        else:
            print(-1)
    elif questr =='size':
        print(len(queue))
    elif questr == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif questr == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif questr == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)