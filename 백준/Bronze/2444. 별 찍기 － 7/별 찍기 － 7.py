N = int(input())
a = 1
b = (2*N)-1
for i in range(1,N+1):
    print(' '* (N-i)+'*' * ((2*i)-1))
    a += 2

for j in range(N-1,0, -1):
    b -= 2 
    print(' ' * (N-j)+'*'* ((2*j)-1) )