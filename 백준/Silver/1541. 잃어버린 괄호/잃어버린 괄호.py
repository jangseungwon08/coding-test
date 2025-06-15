line = input().split("-")
# -로 분리 --> 탐욕 선택 속성 
num = list()
# + 부분을 모두 더해준다.
for i in line:
    if "+" in i:
        temp = i.split("+")
        num_sum = 0
        for i in temp:
            num_sum += int(i)
        num.append(num_sum)
    else:
        num.append(int(i))
ans = num[0]
for i in range(1,len(num)):
    ans -= num[i]
print(ans)