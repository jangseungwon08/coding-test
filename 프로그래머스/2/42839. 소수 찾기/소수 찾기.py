from itertools import permutations
def solution(numbers):
    answer = 0
    num_list = [int(i) for i in numbers]
    comb_num = list(set(int("".join(map(str, p))) for i in range(1,len(num_list) +1) for p in permutations(num_list, i)))
    for i in comb_num:
        if isPrime(i):
            answer += 1
    return answer

def isPrime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True