a, b = map(int, input().strip().split(' '))
for j in range(b):
    for i in range(a):
        #b가 3이고 a가 5이니까 별을 5열 3행으로 찍는다는 소리다.
        #따라서 range(a)에 별을 넣는 함수를 만든다. end = ''을 사용하여 개행하지 않게 한다.
        print("*", end = '')
        #print()의 일반적으로는 개행을 하기 때문에 *을 a범위만큼 찍고 개행을 한다.
        #따라서 *****을 하고 개행을 한다는 소리이다.
    print()