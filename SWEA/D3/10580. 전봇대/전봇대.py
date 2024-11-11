T = int(input())
for tc in range(1,T+1):
    N = int(input())
    #A점과 B점 구하기 위한 빈 리스트 두개 선언
    A_list, B_list = [], []
    #count 0으로 설정
    count = 0
    #N범위 순회하면서
    for _ in range(N):
        #A와 B값을 받아서
        A, B = map(int, input().split())
        #A리스트와 B리스트에 저장
        A_list.append(A)
        B_list.append(B)
    #N-2번째 까지 순회하면서
    for i in range(N-1):
        #i+1부터 N-1번째 까지 순회하면서
        for j in range(i+1, N):
            #A_list의 i번째가 j번째보다 작고 B_list i번째가 j번째 보다 작거나
            #ex) 1일때와 10일때 5 7 다 순회
            if (A_list[i] > A_list[j] and B_list[i] < B_list[j] or A_list[i]
                    < A_list[j] and B_list[i] > B_list[j]):
                count += 1
    print('#'+str(tc), count)
    
    ###완전탐색 문제이다