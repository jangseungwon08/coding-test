a = int(input())
a_list = list(map(int, input().split()))
result = [-1] * a
stack = []
for i in range(a):
    while stack and a_list[stack[-1]] < a_list[i]:
        idx = stack.pop()
        result[idx] = a_list[i]
    stack.append(i)
print(*result)