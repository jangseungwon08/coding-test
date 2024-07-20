def solution(myString):
    answer = []
    #split함수를 사용하여 for문을 돌려서 i의 길이를 구하여 append함수를 사용하여 answer에 추가
    for i in myString.split('x'):
        answer.append(len(i))
    return answer