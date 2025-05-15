import sys
input = sys.stdin.readline
N , M = map(int, input().split())
N_list = list(map(int,input().split()))
remainder= [0] * M
sum = 0
for i in range(N):
    sum += N_list[i]
    remainder[sum % M] += 1
res = remainder[0]

for i in remainder:
    res += i * (i-1) // 2
print(res)