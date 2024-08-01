def solution(arr):
    answer = []
    #arr길이와 비교를 위해서 cnt변수 0부터 설정(2의 거듭제곱 0도 가능하니까)
    cnt = 0
    #len(arr)이 2의 거듭제곱이 아닐때 까지
    while len(arr) != 2**cnt:
        #arr길이와 2**cnt의 값이 같으면 break
        if len(arr) == 2**cnt:
            break
            #arr길이가 더 길면 
        if len(arr) > 2**cnt:
            #cnt 1증가
            cnt += 1
            #2**cnt가 더 길어지면
        else:
            #2**cnt에 arr길이를 뺀 값을 temp에 저장
            temp = 2**cnt - len(arr)
            #temp범위만큼 for문 순회
            for _ in range(temp):
                #arr에 0추가
                arr.append(0)
    return arr
