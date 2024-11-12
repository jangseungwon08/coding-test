T = int(input())
for tc in range(1, T+1):
    s = input()
    half_length = (len(s)-1) //2
    #reversed함수를 사용한 뒤에 값을 띄우려면 ''.join함수 사용해야됨
    reversed_s = ''.join(reversed(s))
    start_s = s[:half_length]
    reversed_start = ''.join(reversed(start_s))
    end_s = s[half_length+1:]
    reversed_end = ''.join(reversed(end_s))
    if s == reversed_s:
        if start_s == reversed_start:
            if end_s == reversed_end:
                print('#'+str(tc), "YES")
            else:
                print('#'+str(tc), "NO")
        else:
            print('#'+str(tc), "NO")
    else:
        print('#'+str(tc), "NO")