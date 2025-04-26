T = int(input())
for i in range(1,T+1):
    stack = []
    s = input()
    ans = 0
    for j in s:
        if j == '(' or j == '{':
            stack.append(j)
        if j == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                ans += 1
        if j == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                ans += 1
    if not stack and ans == 0:
        print('#'+str(i),1)
    else:
        print('#'+str(i),0)