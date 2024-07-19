def solution(todo_list, finished):
    answer = []
    #todo_list의 인덱스 값과 finished의 false 인덱스 값이 같아야되므로 
    # todo_list를 인덱스 형식으로 접근하도록 하기위해서 range(len())을 사용
    for i in range(len(todo_list)):
        #finished[i]의 원소값이 False이면 
        if finished[i] == False:
            #answer에 todo_list[i]를 append함수를 사용하여 대입해준다.
            answer.append(todo_list[i])
    return answer