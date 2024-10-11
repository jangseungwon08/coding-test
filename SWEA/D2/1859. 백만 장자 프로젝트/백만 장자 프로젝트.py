T= int(input())
for i in range(T):
    N = int(input())
    n_list = list(map(int,input().split()))
    max_price = 0
    sum = 0
    for j in range(N-1, -1, -1):
        if n_list[j] > max_price:
            max_price = n_list[j]
        else:
            sum += max_price - n_list[j]
    print('#'+str(i+1), sum)