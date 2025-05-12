N = int(input())
def fib(n):
    f = [0] * (n+1)
    f[1], f[2] = 1, 1
    for i in range(3,n+1):
        f[i] = f[i-1] + f[i-2]
    return f[i]
def dpfib(n):
    return n-2
print(fib(N), dpfib(N))