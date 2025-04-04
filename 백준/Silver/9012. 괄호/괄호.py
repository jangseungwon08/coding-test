import sys
input = sys.stdin.readline
N = int(input().strip())
for _ in range(N):
    N_list = []
    case = input().strip()
    state = True
    for i in case:
        if i == '(':
            N_list.append(i)
        else:
            if N_list:
                N_list.pop(-1)
            else:
                print("NO")
                break
    else:
        if  not N_list:
            print("YES")
        elif N_list:
            print("NO")
