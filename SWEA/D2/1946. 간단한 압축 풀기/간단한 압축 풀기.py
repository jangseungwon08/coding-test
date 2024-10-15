T = int(input())
for i in range(1,T+1):
    N = int(input())
    #문자열을 다 넣기위한 all문자열 
    all = ''
    print('#'+str(i))
    #N만큼 순회하면서
    for _ in range(N):
        #ci값과 ki값을 입력받음
        ci , ki = input().split()
        #all에 ci에 int(ki)를 곱한값을 all에 누적저장
        all += ci*int(ki)
        #0부터len(all)까지 10step씩 순회하면서
    for j in range(0,len(all), 10):
        #all의 j부터 j+10까지 출력
        print(all[j:j+10])
        #j가 0 이면 0부터 9인덱스까지 원소를 출력
        #그 다음step은 10인덱스부터 19까지 원소출력