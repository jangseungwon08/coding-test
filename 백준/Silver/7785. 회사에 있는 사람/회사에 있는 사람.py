n = int(input())
n_dic = dict()
ans_list = []
for _ in range(n):
    name, enter= input().split()
    n_dic[name] = enter
for i in n_dic.keys():
    if n_dic.get(i) == "enter":
        ans_list.append(i)
ans_list = sorted(ans_list, reverse = True)
for i in ans_list:
    print(i)