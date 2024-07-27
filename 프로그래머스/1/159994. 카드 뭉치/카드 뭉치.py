def solution(cards1, cards2, goal):
    answer = 'Yes'
    #goal의 리스트 원소값을 하나씩 돌면서
    for i in goal:
        #cards1이 비어있지 않고 cards1[0]의 값이 i와 같으면
        if cards1 and cards1[0] == i:
            #cards1의 0번째 인덱스 제거
            cards1.pop(0)
            #cards2가 비어있지 않고 cards2[0]의 값이 i와 같으면
        elif cards2 and cards2[0] == i:
            #cards2 0번째 인덱스 제거
            cards2.pop(0)
            #두개의 조건문 만족 못하면 No리턴
        else:
            answer = 'No'
        #정상적으로 for문을 다 순회했으면 Yes리턴
    return answer