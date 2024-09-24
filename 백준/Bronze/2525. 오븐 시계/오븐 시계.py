a, b = map(int, input().split())  # 시와 분을 입력받음
c = int(input())  # 추가할 분을 입력받음

a += c // 60
b += c % 60
if b >= 60:
    a += 1
    b -= 60
    
if a >= 24:
    a -= 24
print(a,b)