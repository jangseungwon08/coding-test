M = int(input())
N = int(input())
sum_list = []
#M부터 N까지 순회하면서
for i in range(M, N+1):
    #M부터 받은 숫자 i가 소수인지 판별하기 위하여
    #2부터 i까지 순회하면서
    for j in range(2,i+1):
        #i에 j를 나눈 나머지가 0이면 
        if i % j == 0:
            #i 와 j가 같으면(즉 1과 자기자신을 제외한 나머지 숫자들이 나눠지면 break)
            if i == j:
#즉, i가 j에 나눈 나머지값이 0이고, i와 j가 같으면 소수로 판정
                #sum_list에 i를 append
                sum_list.append(i)
            #i가 j에 나눠떨어지면 더이상 소수가 아니기때문에 break    
            break
if sum_list:
    print(sum(sum_list))
    print(sum_list[0])
else:
    print(-1)