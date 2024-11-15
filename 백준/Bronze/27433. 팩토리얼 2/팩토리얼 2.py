def recur(n):
    #n이 1이거나 0이면 ans = 1
    if n <= 1:
        ans = 1
    #ans가 2이상이면 recur
    else:
        ans = recur(n-1) * n
    return ans
print(recur(int(input())))