a, b, c = map(int, input().split())
#서로 다른 주사위가 나오는 경우에 가장 큰 눈을 구하기 위해서 list형식
abc_list = [a,b,c]
#abc가 다 같으면
if a == b == c:
    print(10000+(a*1000))
#if 부터 elif까지는 같은 눈이 2개만 나오는 경우의 수 3개의 수가 주어졌으니
#3가지의 경우의 수가 나옴
elif a==b or b==c or c==a:
    if a==b:
        print(1000+(a*100))
    elif b==c:
        print(1000+(b*100))
    else:
        print(1000+(c*100))
    #모두 다른 눈이 나오는 경우
else:
    print(max(abc_list)*100)