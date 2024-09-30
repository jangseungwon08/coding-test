#첫번째 줄에 문자열을 입력받아서 정수형으로 형 변환
T = int(input())
#T범위만큼 순회돌면서
for i in range(T):
    #공백을 기준으로 두 문자열을 입력받아서 정수형으로 변환한 값을 a, b로 저장
    a, b = map(int, input().split())
    #%s로 문자열 포멧팅을 하여서 i+1과 a와 b a+b를 문자열로 출력
    print('Case #%s: %s + %s = %s'%(i+1, a , b, a+b))