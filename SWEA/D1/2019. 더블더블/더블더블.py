N = int(input())
ans = 0
for i in range(N+1):
    if i == 0:
        print(ans+1, end = ' ')
        ans += 1
    else:
        print(ans * 2, end = ' ')
        ans *= 2