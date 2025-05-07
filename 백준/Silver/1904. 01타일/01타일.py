N = int(input())
memo = [1,2,3]
if N <= 3:
    print(memo[N-1])
else:
    for i in range(4,N+1):
        memo.append((memo[i-2] + memo[i-3]) % 15746)
    print(memo[-1])