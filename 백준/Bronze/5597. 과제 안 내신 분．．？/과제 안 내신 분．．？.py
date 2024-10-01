n_list = []
for _ in range(28):
    n_list += [int(input())]
for i in range(1, 31):
    if i not in n_list:
        print(i)