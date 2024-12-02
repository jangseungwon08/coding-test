from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
n_list = deque()
for _ in range(n):
    s = input().strip()
    if s[:4] == 'push':
        n_list.append(int(s[5:]))
    elif s == 'pop':
        if n_list:
            print(n_list.popleft())
        else:
            print(-1)
    elif s == 'size':
        print(len(n_list))
    elif s== 'empty':
        if n_list:
            print(0)
        else:
            print(1)
    elif s == 'front':
        if not n_list:
            print(-1)
        else:
            print(n_list[0])
    elif s == 'back':
        if not n_list:
            print(-1)
        else:
            print(n_list[-1])