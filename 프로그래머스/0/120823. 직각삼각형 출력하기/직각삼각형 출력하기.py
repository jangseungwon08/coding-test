n = int(input())
#별이 시작이 *부터니까 1부터 3번째줄까지 출력 되니까 n의 값까지 출력하려면 range(n+1)
for i in range(1, n+1):
    #'*'*i를 해준다.
    print('*'*i)