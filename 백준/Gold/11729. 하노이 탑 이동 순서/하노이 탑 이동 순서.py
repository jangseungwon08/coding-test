N = int(input())
def recur(n ,start, end):
    if n == 1:
        print(start, end)
        return
    recur(n-1,start, 6-start-end)
    print(start, end)
    recur(n-1,6-start-end, end)
print(2**N -1)
recur(N,1,3)

