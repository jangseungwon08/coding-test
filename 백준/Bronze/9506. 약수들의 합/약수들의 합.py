while True:
    #무한반복으로 n 입력받고
    n = int(input())
    #예외처리 -1이 나오면 루프 종료
    if n == -1:
        break
    #약수를 담을 리스트 선언
    n_list = []
    #1부터 n까지 순회하면서
    for i in range(1,n+1):
        #n % i 의 값이 0 나머지가 없으면 즉 약수이고 , n이 i보다 클때만
        if n % i == 0 and n > i:
            #n_list에 i 추가
            n_list.append(i)
    #루프 끝나고 n_list의 합이 n과 같으면
    if sum(n_list) == n:
        #n =
        print(n, '=', end = ' ')
        #print문에서 *n_list를 하면 n_list원소가 차례대로 출력
        #sep 함수를 사용하여 출력하는 원소를 +로 분리하여 출력
        print(*n_list, sep = ' + ')
    #sum(n_list)와 n의 개수가 다르면
    else:
        #n is NOT perfect 출력
        print(n, 'is NOT perfect.')