import sys
input = sys.stdin.readline
N = int(input())
p = []
for _ in range(N):
    p.append(list(map(int,input().split())))
for i in range(1,N):
    for j in range(len(p[i])):
        if j == 0:
            p[i][j] += p[i-1][j]
            # p의 i번째 행의 길이 -1 ==> 끝 인덱스
        elif j == len(p[i])-1:
            p[i][j] += p[i-1][j-1]
        else:
            p[i][j] += max(p[i-1][j-1], p[i-1][j])
    #마지막 라인만 비교하면되니까까
print(max(p[N-1]))
