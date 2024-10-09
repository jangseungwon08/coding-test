n = int(input())# 색종이의 개수
arr = [[0] * 101 for _ in range(101)] # 도화지의 크기 전부 0 으로 채움
#n의 개수만큼 순회하면서
for _ in range(n):
    #x지점과 y지점을 정수형으로 입력받음
    x, y = map(int,input().split())
    #x지점부터 x+9지점까지 순회하면서
    for i in range(x, x+10):
        #y지점부터 y+9지점까지 순회하면서
        for j in range(y, y+10):
            #y열부터 1로 채움 그 다음 x 증가시키면서 y열 채움
            arr[i][j] = 1
#정답값을 위한 ans 초기화
ans = 0
#2차원배열 arr 순회하면서
for i in arr:
    #1차원 배열의 i의 합을 ans에 누적저장
    ans += sum(i)
#for문 순회 끝내고 ans출력
print(ans)