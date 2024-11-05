N, M = map(int,input().split())
s = list()
count = 0
for _ in range(N):
    s.append(input())
for _ in range(M):
    input_str = input()
    if input_str in set(s):
        count += 1
print(count)