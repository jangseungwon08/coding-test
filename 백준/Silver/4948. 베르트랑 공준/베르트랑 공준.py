import math
import sys
input = sys.stdin.readline
# 에라토스테네스의 체 
def prime(n):
    # 2부터 sqrt(n) + 1 ==> sqrt(n)까지 
    # 왜? -> 만약 2n이 20이면 1 2 4 5 10 20인데
    # sqrt(20)은 4.xx이다. 그러므로 4까지 구하면 좌우 완벽 대칭이 되는 것이다.
    for i in range(2, int(math.sqrt(n))+1):
        if prime_list[i] == True:
            j = 2
            while i * j <= n:
                prime_list[i*j] = False
                j += 1
prime_list = [True] * ((123456 * 2)+1)
prime_list[0], prime_list[1] = False, False
prime(123456*2)
while True:
    n = int(input())
    if n == 0:
        break
    n2 = 2*n
    print(sum(prime_list[n+1:n2+1]))