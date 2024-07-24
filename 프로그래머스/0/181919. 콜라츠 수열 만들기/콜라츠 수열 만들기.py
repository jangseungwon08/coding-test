def solution(n):
    answer = []
    #가장 초기값이 n인 콜라츠 수열 return해야하니까 초기값 n에 저장
    answer.append(n)
    #n이 1일때 까지(n 이 1이 아니면 true이기 때문에 루프 계속 돔)
    while n != 1:
        # n이 짝수 일때
        if n % 2 == 0:
            #answer리스트에 n정수형 나누기 2를 한 값을 append
            answer.append(n // 2)
            #값 업데이트를 위해 n//2를 n에 저장
            n = n//2
            #홀수 일때
        else:
            #answer에 (3*n)+1을 append한 값 저장
            answer.append((3*n)+1)
            #n값 업데이트를 위해 3*n+1을 n에 저장
            n = (3*n) + 1
    return answer