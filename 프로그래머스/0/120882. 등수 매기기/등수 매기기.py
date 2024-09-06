def solution(score):
    answer = []
    #평균 저장 리스트
    average = []
    #score순회하면서
    for i in score:
        #각 영어 점수와 수학점수의 평균치를 average에 append
        average.append((i[0] + i[1])/2)
    #average내림차순으로 정렬
    sorted_avg = sorted(average, reverse = True)
    #average순회하면서
    for j in average:
        #정렬된 평균 리스트에 average의 원소값의 인덱스값을 찾아서 +1 시켜준다.
        #이렇게 하면 동점자도 같은 원소값이라 인덱스값이 같아져 중복처리 가능
        answer.append(sorted_avg.index(j)+1)
    return answer