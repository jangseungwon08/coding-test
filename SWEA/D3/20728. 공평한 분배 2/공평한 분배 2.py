T= int(input())
for tc in range(1,T+1):
    N, K = map(int, input().split())
    N_list = list(map(int, input().split()))
    #N_list에 있는 주머니 속 사탕을 K개씩 집어서 나눠준다는 뜻
    #따라서 선택한 K개 중 최대값과 최소값의 차이가 가장 작은 것을 출력
    #sorted함수 사용하여 N_list를 정렬한다.
    N2_list = sorted(N_list)
    answer = []
    #0부터 N-K+1까지 순회하면서(i+K-1을 하기위해서는 N-K+1을 해줘야됨)
    for i in range(N-K+1):
        #여기서 N2_list의 i+k-1은 정렬된 리스트에서 최대값
        #N2_list[i]는 정렬된 리스트에서 최소값
        diff = N2_list[i+K-1] - N2_list[i]
        #answer배열에 diff값 추가
        answer.append(diff)
    #완전탐색이 끝나고 가장 작은 answer값 출력
    print('#'+str(tc), min(answer))