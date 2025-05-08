N = int(input())
#연산횟수를 저장하는 memo
memo = [0] * (N+1)
for i in range(2,N+1):
    #이전값에서 1을 뺀 값을 연산횟수로 칭함
    memo[i] = memo[i-1] +1
    # i가 2로 나누어떨어지면(2를 1로만드는 최소 연산횟수를 구함)
    if i % 2== 0:
        memo[i] = min(memo[i], memo[i // 2] + 1)
    if i % 3 == 0:
        memo[i] = min(memo[i], memo[i // 3] + 1)
print(memo[N])
