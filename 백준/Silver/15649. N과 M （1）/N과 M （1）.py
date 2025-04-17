import sys
input = sys.stdin.readline
N, M = map(int, input().split())
ans = []

def backtracking():
    if len(ans) == M:
        print(" ".join(map(str, ans)))
        return
    # 1 2 3 4
    for i in range(1, N+1):
        # 1일때
        # ans는 빈배열이니 ans에 1 append
        if i not in ans: #중복확인
            ans.append(i)
            backtracking()
            ans.pop()
backtracking()