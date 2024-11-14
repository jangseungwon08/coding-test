for tc in range(1,11):
    dump = int(input())
    #상자의 높이 리스트
    height_list = list(map(int,input().split()))
    for _ in range(dump):
        if max(height_list) - min(height_list) == 0 or max(height_list) - min(height_list) == 1:
            print('#'+str(tc), max(height_list) - min(height_list))
        else:
            mx_h = height_list.index(max(height_list))
            mn_h = height_list.index(min(height_list))
            height_list[mx_h] = height_list[mx_h] - 1
            height_list[mn_h] = height_list[mn_h] + 1
    print('#'+str(tc), max(height_list) - min(height_list))