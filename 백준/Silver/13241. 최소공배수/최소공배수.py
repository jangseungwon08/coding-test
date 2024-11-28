a, b = map(int, input().split())
def lcm(a,b):
    while b> 0:
        a, b = b, a%b
    return a
def gcd(a,b):
    return a * b/ lcm(a,b)
print(int(gcd(a,b)))