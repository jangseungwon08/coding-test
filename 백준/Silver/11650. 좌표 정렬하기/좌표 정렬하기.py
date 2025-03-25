import sys
input = sys.stdin.readline
N = int(input())
N_list = []
for _ in range(N):
    x, y = map(int, input().split())
    #튜플은 요소값 변경이 불가능하다는 list와의 차이점이 있음
    N_list.append((x,y))
#N_list.sort() #이렇게 짜도 되고
#좀 더 직관적으로 구성하고싶으면
N_list.sort(key = lambda x:(x[0],x[1]))
for x, y in N_list:
    print(x,y)