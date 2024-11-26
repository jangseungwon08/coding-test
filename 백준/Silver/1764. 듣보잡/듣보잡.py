n, m = map(int, input().split())
n_set = set()
ans_list = []
for _ in range(n):
    n_set.add(input())
for _ in range(m):
    name = input()
    if name in n_set:
        ans_list.append(name)
ans_list = sorted(ans_list)
print(len(ans_list))
for i in ans_list:
    print(i)