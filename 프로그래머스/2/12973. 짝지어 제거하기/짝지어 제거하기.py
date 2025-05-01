def solution(s):
    #이 문제 stack 자료구조 문제이다.
    temp = []
    for i in s:
        #1. temp배열이 비어있으면 append
        #2. temp의 마지막 원소가 i이면 temp 제거(바로 다음 문자가 마지막으로 넣은 값과 같으면 제거)
        #3. 배열이 비어있지도 않고 temp의 마지막 원소도 i가 아니면 append
        #    ---> 연결되어있지 않는 문자를 넣어놓고 나중에 문자열을 비교하기 위해서
        if len(temp) == 0:
            temp.append(i)
        elif temp[-1] == i:
            temp.pop()
        else:
            temp.append(i)
    if len(temp) == 0:
        return 1
    else:
        return 0