for tc in range(1,11):
    N = int(input())
    N_list = []
    count = 0
    for _ in range(8):
        N_list.append(input())
    #가로
    for i in range(8):
        for j in range(9-N):
            s = N_list[i][j:N+j]
            reverse_s = s[::-1]
            if s == reverse_s:
                count += 1
    #세로
    #row값 고정
    for i in range(8):
        #col값 j 0부터 8-N까지
        for j in range(9-N):
            #j 부터 j+N까지 순회하면서 k번째 행의 값, i번째 열의 값을 join
            #문 활용하여 s에 저장
            s = ''.join(N_list[k][i] for k in range(j, j+N))
            #reverse_s 는 s의 역순
            reverse_s = s[::-1]
            #s가 reverse_s와 같으면
            if s == reverse_s:
                #count값 증가
                count += 1
    print('#'+str(tc), count)