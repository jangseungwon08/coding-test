T= int(input())
for i in range(1,T+1):
    N = int(input())
    N_list = list(map(int, input().split()))
    N_list.sort()
    print('#'+str(i), end= ' ')
    for j in N_list:
        print(j, end= ' ')
    print()