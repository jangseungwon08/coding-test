def solution(brown, yellow):
    divide_pairs = divide(brown+yellow)
    for i in divide_pairs:
        if (i[0] - 2) * (i[1] - 2) == yellow and i[0] >= i[1]:
            return i

def divide(num):
    divide_pairs = []
    for i in range(int(num**0.5),num+1):
        if num % i == 0:
            divide_pairs.append((i, num // i))
    return divide_pairs