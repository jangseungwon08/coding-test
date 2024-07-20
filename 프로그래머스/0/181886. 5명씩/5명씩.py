def solution(names): 
    answer = []
    #0부터 len(names)-1길이까지 5step씩 늘어나는 for문을 만들어준다.
    for i in range(0, len(names), 5):
        #five변수에 names[i번째부터 i+4번째 인덱스까지] 접근한다.
        five = names[i: i+5]
        #answer에 five변수의 가장앞에있는 사람의 이름을 담은 리스트를 반환 해야하므로 
        #five리스트에 젤 처음인덱스 0을 추가해준다.
        answer.append(five[0])
    return answer