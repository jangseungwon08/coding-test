import sys
input = sys.stdin.readline
N, K = map(int, input().split())
# 5 2 -> 5 4 / 2 1  ==> N! / K!
comb_count = 0
combN = 1
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
factK = factorial(K)
while comb_count < K:
    comb_count += 1
    combN *= N
    N -= 1
print(combN // factK)