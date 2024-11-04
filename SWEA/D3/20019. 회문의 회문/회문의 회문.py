T = int(input())
for i in range(1, T+1):
    t_str = input()
    s_t_str = t_str[:(len(t_str)-1)//2]
    e_t_str = t_str[len(t_str) - ((len(t_str)-1)//2):]
    reverse_str = ''.join(reversed(t_str))
    reverse_s_t_str = ''.join(reversed(s_t_str))
    reverse_e_t_str = ''.join(reversed(e_t_str))
    if t_str == reverse_str:
        if s_t_str == reverse_s_t_str:
            if e_t_str == reverse_e_t_str:
                print('#'+str(i), "YES")
            else:
                print('#'+str(i), "NO")
        else:
            print('#' + str(i), "NO")
    else:
        print('#' + str(i), "NO")