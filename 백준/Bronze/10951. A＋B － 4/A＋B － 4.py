#무한반복으로
while True:
    #try안의 코드를 일단 실행
    try:
        #a, b 를 정수형으로 입력받음
        a, b = map(int,input().split())
        print(a+b)
    #try코드가 실행되지 않을경우 except안의 명령어 수행
    except:
        break