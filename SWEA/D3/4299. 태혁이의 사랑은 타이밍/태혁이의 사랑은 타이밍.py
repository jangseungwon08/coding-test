T = int(input())
totalm = (11* 60 * 24) + (11 * 60) + 11
for tc in range(1,T+1):
    D, H , M = map(int, input().split())
    totalM = (D*60*24) + (H*60) + M
    if totalM >= totalm:
        print('#' + str(tc), totalM - totalm)
    else:
        print('#'+str(tc), -1)
           
