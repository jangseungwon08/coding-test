T = int(input())
for i in range(T):
    str1 = input()
    str2 = input()
    N_dict  = {}
    for j in str1:
        N_dict[j] = 0
    for k in str2:
        if k in N_dict:
            N_dict[k] += 1
    print('#'+str(i+1), max(N_dict.values()))