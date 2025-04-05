import sys
while(True):
    input = sys.stdin.readline().rstrip()
    N_list = []
    if input == '.':
        break
    for i in input:
        if i == '(' or  i == '[':
            N_list.append(i)
        elif i == ')':
            if N_list and N_list[-1] == '(':
                N_list.pop(-1)
            else:
                print('no')
                break
        elif i == ']':
            if N_list and N_list[-1] == '[':
                N_list.pop(-1)
            else:
                print("no")
                break
    else:
        if N_list:
            print("no")
        else:
            print("yes") 