T = int(input())
alpha_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
              'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for tc in range(1, T+1):
    s = input()
    count = 0
    for i in range(len(s)):
        if s[i] == alpha_list[i]:
            count += 1
        else:
            break
    print('#'+str(tc), count)