#실패율은 다음과 같이 정의한다.
#스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
#만약 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 하면 된다.
#스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의한다.
def solution(N, stages):
    answer = []
    temp = {}
    temp2 = []
    user = len(stages)
    stages.sort()
    for i in range(1,N+1):
        not_clear = stages.count(i)
        if i in stages:
            if user > 0:
                if i not in temp2:
                    temp.update({i: not_clear/user})
                    temp2.append(i)
                    user -= not_clear
        else:
            temp.update({i: not_clear})
            temp2.append(i)
    temp = sorted(temp.items(), key = lambda x: x[1] , reverse = True)
    for i in temp:
        answer.append(i[0])
    return answer