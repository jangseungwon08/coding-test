a, b = map(int,input().split())
c, d = map(int,input().split())
#분모 합
f = b * d
#분자 합 
e = (a*d) + (b*c)
def gcd(a,b):
    while b > 0:
        a, b = b, a % b
    return a
def lcm(a,b):
    return a *b // gcd(a,b)
v = gcd(e,f)
f //= v
e //= v
print(e,f)