import sys
input = sys.stdin.readline
N = int(input())
a_list = list()
for _ in range(N):
    s_time, e_time = map(int,input().split())
    a_list.append((s_time, e_time))
a_list = sorted(a_list, key = lambda x:(x[1],x[0]))
init = a_list[0]
ans = 1
for i in range(1, len(a_list)):
    if init[1] <= a_list[i][0]:
        init = a_list[i]
        ans += 1
print(ans)