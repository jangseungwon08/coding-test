import sys
input = sys.stdin.readline
N = int(input())
N_list = list()
for _ in range(N):
    N_list.append(input())

# n은 사각형 크기, y,x는 사각형 시작좌표
def quad_tree(n,y,x):
    for i in range(y, y+n):
        for j in range(x, x+n):
            if N_list[y][x] != N_list[i][j]:
                half_n = n//2
                result = '('
                result += quad_tree(half_n, y,x)
                result += quad_tree(half_n,y, x+ half_n)
                result += quad_tree(half_n, y+ half_n, x)
                result += quad_tree(half_n, y+half_n, x+ half_n)
                result += ')'
                return result
    return N_list[i][j]
print(quad_tree(N,0,0))