a, b = map(int, input().split())
a_list = set(map(int,input().split()))
b_list = set(map(int,input().split()))
ans_list = []
for i in a_list:
    if i not in b_list:
        ans_list.append(i)
for j in b_list:
    if j not in a_list:
        ans_list.append(i)
print(len(ans_list))