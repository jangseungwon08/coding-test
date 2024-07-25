def solution(my_string):
    answer = []
    #my_string을 for문을 돌면서
    for i in my_string:
        #i가 숫자인지 판별 만약 True이면 숫자라는 뜻이니까
        if i.isdigit():
            #answer배열에 int(i)로 형 변환한 값을 append
            answer.append(int(i))
    #for문을 다 돌린 후 answer오름차순 정렬
    answer.sort()
    return answer