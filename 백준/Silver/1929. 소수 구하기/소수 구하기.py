import sys
import math
input = sys.stdin.readline
M, N = map(int, input().split())
#1과 0은 무조건 True이기 때문
prime = [True for _ in range(N+1)]
prime[0], prime[1] = False, False
for i in range(2, int(math.sqrt(N))+1):
    if prime[i] == True:
        j = 2
        while j * i <= N:
            prime[i*j] = False
            j += 1
for i in range(M, N+1):
    if prime[i] == True:
        print(i)