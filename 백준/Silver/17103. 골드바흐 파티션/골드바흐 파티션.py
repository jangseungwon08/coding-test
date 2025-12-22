import sys
input = sys.stdin.readline
T = int(input())
max = 1000000
list = [True] * (max+1)
for i in range(2, int(max**0.5)+1):
    if list[i]:
        for j in range(i*2, max+1, i):
            list[j] = False
for _ in range(T):
    N = int(input())
    cnt = 0
    for i in range(2, N//2+1):
        if list[i] and list[N-i]:
            cnt += 1
    print(cnt)