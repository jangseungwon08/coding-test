import sys
input = sys.stdin.readline

def recur(n):
    if n == 1:
        return "-"
    stack = recur(n//3)
    res = stack + " "*(n//3) + stack
    return res
while True:
    try:
        N = int(input())
        print(recur(3**N))
    except:
        break
