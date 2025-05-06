T = int(input())
for _ in range(T):
    memo = [1,1,1,2,2]
    N = int(input())
    if N <= 5:
        print(memo[N-1])
    else:
        for i in range(6,N+1):
            memo.append(memo[i-2] + memo[i-6])
        print(memo[-1])