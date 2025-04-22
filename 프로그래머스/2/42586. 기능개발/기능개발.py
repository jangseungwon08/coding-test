from collections import deque
def solution(progresses, speeds):
    temp = deque([])
    answer = []
    for i in range(len(progresses)):
        if (100 - progresses[i]) % speeds[i] == 0: #실수가 아니라는 뜻
            temp.append((100 - progresses[i]) // speeds[i])
        else:
            temp.append(((100 - progresses[i]) // speeds[i])+1)
    while temp:
        count = 1
        #먼저 comple에 popleft하고
        comple = temp.popleft()
        #temp의 길이가 1 이상 --> 남아있는 값이 있을 경우
        #그리고 comple의 값이 temp[0]의 값 보다 클 경우 다음 기능은 완료가 되어도 배포가 안되니
        while len(temp) >= 1 and comple >= temp[0]:
            #temp의 길이가 1이상 그리고 comple의 값이 temp의 0번째 값 보다 클 때 동안
            #temp의 길이가 1 이상?
            temp.popleft()
            count += 1
        answer.append(count)
    return answer