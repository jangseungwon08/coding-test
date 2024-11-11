T= int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    #M을 2진수로 표현하기위해 bin함수 사용하여 2진수로 표현 0b를 제거하기위해 1번째
    #인덱스까지 값 제거
    binary_M = bin(M)[2:]
    #binary_M의 길이 - N만큼 부터 끝까지(뒤에서 N번째까지 이기때문에
    #len(binary_M) - N 해야지 뒤에서 N번째부터가 가능
    s = binary_M[len(binary_M) - N::]
    #나온 s의 값이 '1'*N 즉 모두 1이면 
    if s == '1' * N:
        #ON 출력
        print('#'+str(tc), 'ON')
        #0이 하나라도 있으면 OFF출력
    else:
        print('#'+str(tc), 'OFF')