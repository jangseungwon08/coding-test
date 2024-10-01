N, M = map(int, input().split())
#1부터 N값까지의 수를 가진 N_list생성
N_list = [i for i in range(1,N+1)]
#M만큼 범위 순회하면서
for _ in range(M):
    #i와 j를 입력받아 int형식으로 형 변환
    i, j = map(int, input().split())
    #N_list의 i번째와 j번째 값을 서로 바꿔줌
    N_list[i-1] , N_list[j-1] = N_list[j-1], N_list[i-1]
    #N만큼 범위 순회하면서 N_list의 i값을 개행없이 출력
for i in range(N):
    print(N_list[i], end = ' ')