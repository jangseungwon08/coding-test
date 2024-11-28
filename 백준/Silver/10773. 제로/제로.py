k =  int(input())
arr = []
for _ in range(k):
    a = int(input())
    if a == 0:
        arr.pop(-1)
    else:
        arr.append(a)
print(sum(arr))