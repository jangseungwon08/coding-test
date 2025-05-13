T = int(input())
alpha = "abcdefghijklmnopqrstuvwxyz"
for tc in range(1,T+1):
    compet = input()
    count = 0
    for i in range(len(compet)):
        if compet[i] != alpha[i]:
            break
        else:
            count += 1
    print('#'+str(tc), count)