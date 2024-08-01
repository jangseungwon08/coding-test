def solution(arr):
    answer = []
    cnt = 0
    while len(arr) != 2**cnt:
        if len(arr) == 2**cnt:
            break
        if len(arr) > 2**cnt:
            cnt += 1
        else:
            temp = 2**cnt - len(arr)
            for _ in range(temp):
                arr.append(0)
    return arr