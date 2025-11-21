import sys
from collections import Counter
input = sys.stdin.readline
N = int(input())
num_li = []
for _ in range(N):
    num_li.append(int(input()))
num_li = sorted(num_li)
print(round(sum(num_li)/N))
print(num_li[len(num_li)//2])
counter = Counter(num_li)
mode_value = counter.most_common(2)
if len(mode_value) > 1:
    if mode_value[0][1] == mode_value[1][1]:
        print(mode_value[1][0])
    else:
        print(mode_value[0][0])
else:
    print(mode_value[0][0])
    

print(num_li[-1] - num_li[0])