def solution(n):
    answer = 0
    memo = [1,2,3]
    for i in range(3,n+1):
        memo.append((memo[i-1] + memo[i-2]) % 1234567)
    return memo[n-1]