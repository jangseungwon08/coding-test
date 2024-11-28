t = int(input())
for _ in range(t):
    stack = []
    s = input()
    #s문자열 순회하면서
    for i in s:
        #i가 '('이면 stack에 (문자 append
        if i == '(':
            stack.append('(')
            #i 가 )이고 stack이 비어있지않으면 -> '(' 문자가 있다는 뜻이니
            #stack pop
        elif i == ')':
            if stack:
                stack.pop()
            #stack이 비어있지 않으면 NO프린트한 뒤 루프 탈출
            else:
                print('NO')
                break
            #break문을 끊기지 않고 
        #stack이 비어있으면 이라는 뜻이므로 괄호가 다 알맞게 완성되었다는 뜻
    else:    
        if not stack:
            print('YES')
        #stack이 있으면 괄호가 완성이 안되었다는 뜻
        else:
            print('NO')