import sys
input = sys.stdin.readline

A, B = map(int, input().strip().split())
A_Set = set(list(map(int, input().strip().split())))
B_Set = set(list(map(int, input().strip().split())))
print(len(A_Set-B_Set) + len(B_Set-A_Set))
