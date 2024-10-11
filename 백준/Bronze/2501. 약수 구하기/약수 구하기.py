#N과 K입력받음
N, K = map(int,input().split())
#약수를 넣을 N_list선언
N_list = []
#1부터 N까지 순회하면서
for i in range(1,N+1):
    #N에 i를 나눈 값이 0 즉 i가 N의 약수이면
    if N % i == 0:
        #N_list에 i append
        N_list.append(i)
    #N_list의 길이가 K와 크거나 같으면
if len(N_list) >= K:
    #K-1번째 인덱스값 출력
    print(N_list[K-1])
#N_list의 길이가 K보다 작으면
else:
    #0 출력
    print(0)