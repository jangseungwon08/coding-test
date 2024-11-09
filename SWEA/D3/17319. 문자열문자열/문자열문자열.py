T = int(input())
for tc in range(1,T+1):
    N = int(input())
    s = input()
    new_s = s[:N // 2:]
    if s == new_s *2:
        print('#'+str(tc), "Yes")
    else:
        print('#'+str(tc), "No")