import sys
input = sys.stdin.readline
n = int(input().strip())
n_list = []
for _ in range(n):
    stack_input = input().strip()
    if stack_input[0] == '1':
        n_list.append(int(stack_input[2:]))
    elif stack_input[0] == '2':
        if n_list:
            print(n_list.pop(-1))
        else:
            print(-1)
    elif stack_input[0] == '3':
        print(len(n_list))
    elif stack_input[0] == '4':
        if n_list:
            print(0)
        else:
            print(1)
    elif stack_input[0] == '5':
        if n_list:
            print(n_list[-1])
        else:
            print(-1)