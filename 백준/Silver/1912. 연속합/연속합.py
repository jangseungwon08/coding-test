N = int(input())
N_list = list(map(int,input().split()))
for i in range(1,N):
    # i-1번쨰를 더해주는 이유는 i번쨰 데이터 이전까지 합을 계산했을 때 값과 
    # i번째의 값을 비교하는 것이다.
    # 따라서 i번째 이전까지의 값이 N_list의 원소를 다 더하는 값과 비교해서 최대값이 되는 것
    N_list[i] = max(N_list[i-1] + N_list[i], N_list[i])
print(max(N_list))