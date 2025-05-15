N = int(input())
def recur(n):
    if n == 1:
        return ['*']
    
    stars = recur(n // 3)
    arr = []

    for i in stars:
        arr.append(i*3)
    for i in stars:
        arr.append(i + ' '*(n//3) + i)
    for i in stars:
        arr.append(i*3)
    return arr
print('\n'.join(recur(N)))