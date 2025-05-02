T = int(input())
for i in range(1,T+1):
    N, sixteen = input().split()
    N = int(N)
    res = ""
    for j in sixteen:
        ten = int(j, 16)
        binary = bin(ten)[2:]
        res += binary.zfill(4)
    print('#'+str(i), res)