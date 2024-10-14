T = int(input())
for i in range(1,T+1):
    #10개의 수를 list로 입력받음
    N_list = list(map(int,input().split()))
    #최대수 인덱스위치값 제거
    N_list.pop(N_list.index(max(N_list)))
    #최소수 인덱스위치값 제거
    N_list.pop(N_list.index(min(N_list)))
    #N_list의 합과 N_list의 길이를 나눠줘서 평균을 구함(round함수사용하여 반올림)
    print('#'+str(i), round((sum(N_list)/len(N_list))))