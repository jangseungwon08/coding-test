N, M = map(int, input().split())
#a리스트와 b리스트를 나누기위한 리스트 선언
a, b = [], []
#N-1의 범위만큼 순회하면서
for i in range(N):
    #a리스트에 공백을 기준으로 입력받은 문자열을 정수형으로 형 변환하여
    #list형식으로 append
    a.append(list(map(int, input().split())))
for i in range(N):
    b.append(list(map(int, input().split())))
#i를 행으로 j를 열로 두고 첫번째 행을 기준으로 a의 j열과 b의 j열으 더하여 
#개행하지 않고 출력 j열 덧셈이 끝나면 print()를하여 개행
for i in range(N):
    for j in range(M):
        print(a[i][j] + b[i][j], end = ' ')
    print()