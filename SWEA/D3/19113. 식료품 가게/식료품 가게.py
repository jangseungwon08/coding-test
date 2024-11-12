###완전탐색인데 원소 하나씩 삭제하면서 검색###
T= int(input())
for tc in range(1,T+1):
    N = int(input())
    N_list = list(map(int, input().split()))
    #정답을 위한 ans_list
    ans_list = []
    #0부터 N_list-1길이까지 순회하면서
    for i in range(0,len(N_list)-1):
        #i+1번째부터 N_list까지 순회하면서
        for j in range(i+1,len(N_list)):
            #N_list[j](i+1번째에 0.75를 곱한 값)에 정수형으로 형 변환 한 값이
            #N_list[i]번째 값과 같으면
            if int(N_list[j]*0.75) == N_list[i]:
                #N_list[i]가 25%할인된 가격이라는 뜻이니까 
                #정답 리스트에 N_list[i]를 append
                ans_list.append(N_list[i])
                #N_list에서 원래의 할인전의 값을 제거 후 break
                N_list.pop(j)
                break
    print('#'+str(tc), end= ' ')
    for n in ans_list:
        print(n, end= ' ')
    print()