N, K = map(int, input().split())
arr = list()
for _ in range(N):
    arr.append(int(input()))
arr.sort(reverse = True)
answer = 0
for i in arr:
    # i가 K보다 크면 나눠질 수 있다는 뜻이므로 
    if K >= i:
        # answer에 k에 i를 나눈 값을 저장
        answer += K // i
        # 나눈 나머지로 K업데이트 해줌
        K = K % i
        # K가 0이면 종료 (종료조건)-> K가 0이 되었으니 구할 수 없음
        if K == 0:
            break
print(answer)