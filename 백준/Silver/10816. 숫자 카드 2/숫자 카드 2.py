n = int(input())
n_list = list(map(int,input().split()))
m = int(input())
m_list = list(map(int,input().split()))
ans_list = []
n_dict = dict()
for i in n_list:
    if i in n_dict:
        n_dict[i] += 1
    else:
        n_dict[i] = 1
for i in m_list:
    if i in n_dict:
        print(n_dict[i], end = ' ')
    else:
        print(0, end = ' ')