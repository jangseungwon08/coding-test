a = int(input())
a_list = list(map(int, input().split()))
res = [-1] * a
a_dict = dict()
stack = []
for i in a_list:
    if i in a_dict:
        a_dict[i] += 1
    else:
        a_dict[i] = 1
for i in range(a):
    while stack and a_dict[a_list[stack[-1]]] < a_dict[a_list[i]]:
        idx = stack.pop()
        res[idx] = a_list[i]
    stack.append(i)
for i in res:
    print(i, end = " ")