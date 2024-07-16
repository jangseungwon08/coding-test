def solution(arr1, arr2):
    answer = []
    #for문을 돌면서 zip(arr1,arr2)은 리스트의 같은 위치에 있는 원소들을 i, j 로 묶어준다.
    for i,j in zip(arr1,arr2):
        #결과 리스트 초기화
        sum =[]
        #for 문을 돌면서 튜플 i,j로 묶은 원소들을 a,b 로 묶어준다.
        #[1,2], [3,4]를 (1,3), (2,4)로  
        for a, b in zip(i,j):
            #이 각 원소의 값을 더한 값을 append를 이용하여 마지막에 붙여준다.
            sum.append(a+b)
            #answer에 append를 이용하여 붙여준다.
        answer.append(sum)
    return answer