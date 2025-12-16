import sys
input = sys.stdin.readline
# n = 나무의 수 , m = 상근이가 집으로 가져가려고 하는 나무의 길이
n, m = map(int, input().split())
# 나무의 높이 리스트
n_list = list(map(int, input().split()))
start, end = 1, max(n_list)
while start <= end:
    mid = (start + end) // 2
    tree_count = 0
    for i in n_list:
        if i > mid:
            tree_count += i - mid
    if tree_count >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)