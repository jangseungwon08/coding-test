N = int(input())
#n-1범위까지 순회하면서 공백은 N-i만큼 출력하고, 별은 i만큼 출력
#공백을 두고 별을 출력 
for i in range(1,N+1):
    print(' '*(N-i)+'*'*(i))