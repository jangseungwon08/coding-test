N = int(input())
divisor = 2
N_list = []
# N이 1이아닐때까지
while N != 1:
    #N 에 divisor를 나눈 나머지가 0이 아니면 소인수가 아니기 때문에
    if N % divisor != 0:
        #divisor에 1 증가
        divisor += 1
    #N에 divisor가 나눠지면
    else:
        #N_list에 divisor를 append
        N_list.append(divisor)
        #N값 업데이트
        N = N// divisor
#N_list순회하면서 i출력
for i in N_list:
    print(i)