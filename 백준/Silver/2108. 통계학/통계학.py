import sys
from collections import Counter
input = sys.stdin.readline
N = int(input())
N_average = 0
middle = 0
middle_idx = N // 2
N_list = []
for _ in range(N):
    N_list.append(int(input()))
N_average = int(round(sum(N_list)/len(N_list)))
N_list.sort()
count = Counter(N_list)
ans_count = []
max_num = max((count.values()))
for k, v in count.items():
    if v == max_num:
        ans_count.append(k)
middle = N_list[middle_idx]
bound = max(N_list) - min(N_list)
ans_count.sort()
print(N_average)
print(middle)
if len(ans_count) > 1:
    print(ans_count[1])
else:
    print(ans_count[0])
print(bound)