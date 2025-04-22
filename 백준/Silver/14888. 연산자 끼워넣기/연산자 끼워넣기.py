import sys
input = sys.stdin.readline
N = int(input())
N_list = list(map(int, input().split()))
operation = list(map(int, input().split()))
mx = -1000000000
mn = 1000000000

def backtracking(depth,temp,plus,minus,multiply,divide):
    global mx,mn
    if depth == N:
        mx = max(temp, mx)
        mn = min(temp, mn)
        #플러스부터 들어가서 모든 경우의 수 검사
    if plus > 0:
        backtracking(depth+1, temp + N_list[depth], plus-1, minus,multiply, divide)
    #마이너스부터 들어가서 모든 경우의 수 검사
    if minus > 0:
        backtracking(depth+1, temp - N_list[depth], plus, minus-1 ,multiply, divide)
    #곱하기부터 들어가서 모든 경우의 수 검사
    if multiply > 0:
        backtracking(depth+1, temp * N_list[depth], plus, minus,multiply-1, divide)
    #나누기부터 들어가서 모든 경우의 수 검사사
    if divide > 0:
        backtracking(depth+1, int(temp / N_list[depth]), plus, minus,multiply, divide-1)
#--> 따라서 모든 경우의 수를 다 접근가능하다.

backtracking(1,N_list[0],operation[0],operation[1],operation[2],operation[3])
print(mx)
print(mn)