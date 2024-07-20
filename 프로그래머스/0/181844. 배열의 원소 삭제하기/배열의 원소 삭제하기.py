def solution(arr, delete_list):
    answer = []
    #arr의 value값들을 알기 위해서 for문 돌린다.
    for i in arr:
        #arr의 value값이 delete_list안에 없으면
        if i not in delete_list:
            #answer배열에 value i를 추가해준다.
            answer.append(i)
    return answer