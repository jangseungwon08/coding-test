T = int(input())
for i in range(1,T+1):
    s= input()
    if s[::] == s[::-1]:
        print('#'+str(i), 1)
    else:
        print('#'+str(i),0)