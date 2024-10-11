N = int(input())
#N범위까지 순회하면서
for i in range(1,N+1):
    #문자열 i에 3 6 9문자의 개수가 얼마나 들어가는지 다 더함
    i = str(i)
    count = i.count('3') + i.count('6') + i.count('9')
    #다 더한 문자열 개수가 0이면 그냥 숫자를 외치는
    if count == 0:
        #i 출력
        print(i, end = ' ')
        #count 개수가 있으면
    else:
        #박수 대신 -*count를 출력
        print('-'*count, end = ' ')