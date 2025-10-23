from itertools import combinations
def solution(nums):
    answer = 0
    nums.sort()
    for iter in combinations(nums, 3):
        if is_prime(sum(iter)):
            answer += 1
    return answer

def is_prime(num):
    end = int(num**0.5)
    for i in range(2, end+1):
        if num % i == 0:
            return False
    return True