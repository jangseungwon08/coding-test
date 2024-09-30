#무한반복으로
while True:
    #a, b 를 정수형으로 입력받음
    a, b = map(int,input().split())
    #a와 b가 0이면 루프탈출
    if a==0 and b==0:
        break
    #0이 아니면 a+b출력
    else:
        print(a+b)