def solution(my_string):
    answer = ''
    #문자열의 원소값들을 임시로 리스트에 넣을 배열 선언
    temp = []
    #my_string순회하면서
    for i in my_string:
        #i번째 값이 temp배열에 없으면
        if i not in temp:
            #차례대로 temp 배열에 i append
            temp.append(i)
    #for문 다 순회 후 배열을 문자열로 바꿔주기 위해서 join함수사용하여 문자열로 변경해준다.
    answer = ''.join(temp)
    return answer