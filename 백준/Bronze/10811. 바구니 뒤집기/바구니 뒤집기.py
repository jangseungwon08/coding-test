#첫째줄에 n과 m을 입력받음
N, M = map(int, input().split())
#n_list의 n만큼의 배열을 만들기위한 for문(n이 5면 1 2 3 4 5이런식)
n_list = [i for i in range(1,N+1)]
#M범위까지 순회하면서
for _ in range(M):
    #i, j를 입력받음
    i, j = map(int,input().split())
    #n_list의 i-1번째부터 j-1번째까지 의 원소들을 temp에 저장
    temp = n_list[i-1:j]
    #temp리스트의 원소값들을 역순으로 만들어내는 함수
    temp.reverse()
    #n_list의 i-1번째부터 j-1번째 원소값들에 변화된 temp값을 저장
    n_list[i-1:j] = temp
    #N번째까지 순회하면서 n_list[i]번째 값들을 출력
for i in range(N):
    print(n_list[i], end = ' ')