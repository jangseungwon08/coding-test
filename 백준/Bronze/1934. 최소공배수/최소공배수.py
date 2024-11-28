t = int(input())
#유클리드 호제법 최대공약수
#gcd(a,b) = gcd(b,a%b)와 같다는 의미이다.
def gcd(a,b):
    #a를 b로 나눈 나머지와 b의 최대공약수는 a와 b의 최대 공약수가 같다는것을
    #의미
    while b> 0:
        a, b = b, a % b
    return a
#최소공배수
#a, b 배수중 a,b의 곱을 a,b의 최대공약수로 나눈 값
def lcm(a,b):
    return a*b / gcd(a,b)
for _ in range(t):
    a, b = map(int,input().split())
    print(int(lcm(a,b)))