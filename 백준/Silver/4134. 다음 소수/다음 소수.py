import math
T = int(input())

def is_prime(num):
    if num == 0 or num == 1:
        return False
    for i in range(2,int(math.sqrt(num))+1):
        if num % i== 0:
            return False
    return True

for _ in range(T):
    N = int(input())
    while True:
        if is_prime(N):
            print(N)
            break
        else:
            N += 1