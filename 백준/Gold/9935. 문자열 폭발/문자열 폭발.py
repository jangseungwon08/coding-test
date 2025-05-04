import sys

input = sys.stdin.readline

S = input().strip()
bomb = input().strip()
temp = []
for i in S:
    temp.append(i)
    if bomb == ''.join(temp[len(temp) - len(bomb):len(temp)]):
        for i in range(len(bomb)):
            temp.pop()
S = temp
if not S:
    print("FRULA")
else:
    print(''.join(S))