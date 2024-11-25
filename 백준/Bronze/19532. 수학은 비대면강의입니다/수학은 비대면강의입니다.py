a, b, c, d, e, f = map(int,input().split())
#-999부터 999까지니까 x를 i로 정함
for i in range(-999, 1000):
    #y를 j로
    for j in range(-999, 1000):
        #a*x + b*y d*x e*y 값이 c와 f와 같은 값이면
        if (a*i) + (b*j) == c and (d*i) + (e*j) == f:
            print(i, j)