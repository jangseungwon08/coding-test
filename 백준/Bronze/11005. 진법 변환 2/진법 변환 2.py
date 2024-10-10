N , B = map(int,input().split())
# 진법 변환을 위한 num_list 생성
num_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#정답을 위한 문자열 선언
ans = ''
#N의 값이 0이 아닐때까지 (N의 값이 1이상이면 루프)
while N != 0:
    #N 에서 B를 나눈 나머지 값을 N_index에 저장
    N_index = N % B 
    #N 정수형 나누기를 한 값으로 N갱신
    N = N // B
    #ans문자열에 num_list에서 N_index값의 원소값을 저장
    ans += num_list[N_index]
#진법은 거꾸로 가야되니까 가장 큰 값에 젤 먼저 나눠 N_index에 저장된 값이 
#가장 뒤로 가야됨(정수 N에 한번 나눈 값이므로 B**0승으로 취급)
#그 뒤로 계속 나눠준 값이 B**1 B**2으로 차례대로 증가
print(ans[::-1])