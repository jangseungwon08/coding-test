def solution(n):
    memo = [0] * (n+1)
    memo[0] = 0
    memo[1] = 1
    for i in range(2,n+1):
        #1234567을 mod하는 이유는 
        #fib(100)만해도 64비트int의 범위를 넘어서기때문에
        #1234567을 하여 나머지를 memo에 저장한다. 
        #단지 값만 보는것이 아닌 overflow를 어떻게 효율적으로 정리하느냐도 보는듯
        memo[i] = (memo[i-1] + memo[i-2]) % 1234567
    return memo[-1]