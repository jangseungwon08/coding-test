T = int(input())
for i in range(1, T+1):
    ori_str = ""
    ans_list = []
    N = int(input())
    for j in range(N):
        alpha, num = input().split()
        ori_str += alpha*int(num)
    for k in range(0, len(ori_str), 10):
        ans_list.append(ori_str[k:k+10])
    print('#'+str(i))
    for l in ans_list:
        print(l)