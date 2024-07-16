def solution(d, budget):
    #d를 부서별 오름차순으로 정렬한다.
    answer = 0
    d.sort()
    #enumerate함수를 사용하여 인덱스 값과 value값을 동시에 가져옴
    for idx, i in enumerate(d):
        #for문을 돌면서 budget에다가 i(value)값을 빼줌
        budget -= i
        #budget값이 0보다 작을 때
        if budget <0:
            #인덱스 값 리턴
            return idx
        #for문을 다 돌면 budget값과 value값이 딱 맞아 떨어진다는 뜻이므로 모든 부서를 지원한다
        #는 뜻이된다. 따라서 d의 길이를 반환
        answer = len(d)
    return answer