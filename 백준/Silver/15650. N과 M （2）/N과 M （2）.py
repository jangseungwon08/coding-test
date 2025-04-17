import sys
input = sys.stdin.readline
N, M = map(int, input().split())
ans = []

def backtracking():
    compet_list = sorted(ans)
    if len(ans) == M and ans == compet_list:
        print(" ".join(map(str, ans)))
        return
    # 1 2 3 4
    for i in range(1, N+1):
        if i not in ans: 
            ans.append(i)
            backtracking()
            ans.pop()
backtracking()