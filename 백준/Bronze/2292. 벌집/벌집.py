#숫자 입력받음
N = int(input())
#처음 숫자에서 시작해야되니까 first를 1로 설정
first = 1
#개수 방을 지나서 갈 때니까 count변수 설정
count = 1
#N이 first값보다 클 때만
while N > first:
    #first주위에 둘러싸인 6각형 층이 1층에 6개가 있기때문에 6을 곱해줌
    first += 6 *count
    #1층에 있는 값을 다 썻기 때문에 count에 1 더해줌
    count += 1
print(count)