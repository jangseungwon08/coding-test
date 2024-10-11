N =int(input())
#역순은 0+1번째까지 정순은 -1까지
#그래서 0까지 출력하려면 -1+1까지 해야지 0까지 나옴
for i in range(N,-1,-1):
    print(i, end = ' ')