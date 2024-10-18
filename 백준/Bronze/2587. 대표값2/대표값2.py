N_list = []
for _ in range(5):
    N_list.append(int(input()))
N_list.sort()
print(sum(N_list)//len(N_list))
print(N_list[2])