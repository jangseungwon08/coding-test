N, M = map(int,input().split())
s = set()
count = 0
for _ in range(N):
    s.add(input())
for _ in range(M):
    input_str = input()
    if input_str in set(s):
        count += 1
print(count)