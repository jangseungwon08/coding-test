T = int(input())
for i in range(1,T+1):
    s = input()
    s_list = []
    for j in range(1,len(s)):
        if s[:j] == s[j:j*2]:
            print('#'+str(i), j)
            break