import sys
input = sys.stdin.readline
N , M = map(int, input().split())
N_list = []
def backtracking():
    if len(N_list) == M:
        print(" ".join(map(str, N_list)))
        return
    for i in range(1,N+1):
        N_list.append(i)
        backtracking()
        N_list.pop()
backtracking()