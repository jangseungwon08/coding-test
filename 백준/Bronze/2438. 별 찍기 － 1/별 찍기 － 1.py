N = int(input())
#n-1범위까지 순회하면서 '*' * (i)면 i가 3이면 별이 3개찍힘
for i in range(N):
    print('*'*(i+1))