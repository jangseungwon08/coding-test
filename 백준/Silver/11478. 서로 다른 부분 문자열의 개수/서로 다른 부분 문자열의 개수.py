s = input()
ans_set = set()
#i 0부터 len(s)까지
for i in range(len(s)):
    #j i번째부터 lens(s)까지
    #i가 7이면 7부터 len(s)-1까지--> i값 고정시켜놓고 j값을 변경시킴
    for j in range(i, len(s)):
        ans_set.add(s[i:j+1])
print(len(ans_set))