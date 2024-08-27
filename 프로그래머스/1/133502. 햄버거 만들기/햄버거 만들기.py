def solution(ingredient):
    answer = 0
    #햄버거를 넣을 임시 리스트
    finish_ham = []
    #ingredient 순회하면서
    for i in ingredient:
        #finish_ham리스트에 i하나씩 붙임
        finish_ham.append(i)
        #finish_ham의 -4번째부터 끝까지 원소값이 1231과 같으면
        if finish_ham[-4:] == [1,2,3,1]:
            #finish_ham 리스트에서 -4번째부터 끝까지 원소 제거
            del finish_ham [-4:]
            #answer 값 1 증가
            answer += 1
    return answer