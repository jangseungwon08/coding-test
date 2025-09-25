# import sys
# input = sys.stdin.readline
N = int(input())

for i in range(1,N+1):
    num = map(int, str(i))
    num_sum = sum(num) + i
    if num_sum == N:
        print(i)
        break
    if i == N:
        print(0)
# 그러니까 216의 분해합이 198이다. 그러니까 198 + 1 + 9+ 8 이 216이 되는 값을 찾는것임
# 216까지 못돌면 분해합이 없다는것이니 0출력