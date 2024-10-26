for tc in range(1,11):
    T = int(input())
    N = list(map(int,input().split()))
    count = 0
    for i in range(2,len(N)-2):
        temp_list = []
        if i == 2:
            if N[i] > N[i+1] and N[i] > N[i+2]:
                temp_list.append(N[i+1])
                temp_list.append(N[i+2])
                count += N[i] - max(temp_list)
            else:
                count += 0
        elif i == (len(N)-2):
            if N[i] > N[i-1] and N[i] > N[i-2]:
                temp_list.append(N[i-1])
                temp_list.append(N[i-2])
                count += N[i] - max(temp_list)            
            else:
                count += 0
        else:
            if N[i] > N[i+1] and N[i] > N[i+2] and N[i] > N[i-1] and N[i] > N[i-2]:
                temp_list.append(N[i+1])
                temp_list.append(N[i+2])
                temp_list.append(N[i-1])
                temp_list.append(N[i-2])
                count += N[i] - max(temp_list)
            else:
                count += 0
    print('#'+str(tc), count)