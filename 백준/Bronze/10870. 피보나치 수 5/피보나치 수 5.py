def fib(n):
    if n <= 1:
        ans = n
    else:
        ans = fib(n-1) + fib(n-2)
    return ans
print(fib(int(input())))